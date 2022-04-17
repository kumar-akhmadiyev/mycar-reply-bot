from django.db import models
from reply_bot.mixins import TimestampMixin
from tg_bot.utils import send_message


class Message(TimestampMixin):
    text = models.CharField('Текст сообщения', max_length=255)
    user = models.ForeignKey(verbose_name='Пользователь',
                             to='users.MainUser',
                             related_name='messages',
                             on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        is_sending = not self.pk and self.user.telegram_chat_id
        super(Message, self).save(*args, **kwargs)
        if is_sending:
            message = f"{self.user.first_name}, я получил от тебя сообщение:\n" \
                      f"{self.text}"
            send_message(self.user.telegram_chat_id, message)
