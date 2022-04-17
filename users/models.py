from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from reply_bot.mixins import TimestampMixin


class MainUser(TimestampMixin, AbstractUser):
    email = models.EmailField('Email', null=True, blank=True)
    access_token = models.UUIDField("UUID идентификатор", default=uuid4, unique=True, editable=False)
    telegram_chat_id = models.CharField(max_length=30, blank=True, null=True)
