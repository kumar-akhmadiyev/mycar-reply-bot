from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tg_bot.models import Message


class MessageSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = ['text', 'created_at']

    def create(self, validated_data):
        user = self.context.get('user')
        message = Message.objects.create(
            text=validated_data.get('text'),
            user=user
        )
        return message
