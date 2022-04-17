from django.urls import path

from tg_bot.views import MessageViewSet, TGWebHookView


urlpatterns = [
    path('list/', MessageViewSet.as_view({'get': 'list'}), name='message-list'),
    path('send/', MessageViewSet.as_view({'post': 'create'}), name='create-message'),
    path('webhook/<str:token>/', TGWebHookView.as_view(), name='webhook')
]
