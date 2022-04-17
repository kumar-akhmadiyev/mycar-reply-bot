from rest_framework import generics, mixins, viewsets, permissions, views
from rest_framework.response import Response
from django.conf import settings
from telegram import Update

from tg_bot.models import Message
from tg_bot.serializers import MessageSerializer
from tg_bot.utils import updater


class MessageViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        context['user'] = request.user
        serializer = self.get_serializer_class()(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TGBotWebHookView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        token = kwargs.get("token")
        if token != settings.TELEGRAM_WEBHOOK_TOKEN:
            return Response(status=400)

        update = Update.de_json(request.data, updater.bot)
        updater.dispatcher.process_update(update)

        return Response(status=200)
