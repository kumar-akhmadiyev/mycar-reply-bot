import logging
import uuid

from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update
from django.conf import settings
from django.core.exceptions import ValidationError

from users.models import MainUser


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token=settings.TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def run_bot():
    logging.warning("IN RUN BOT")
    token = settings.TELEGRAM_WEBHOOK_TOKEN
    url = f"{settings.BASE_URL}messages/webhook/{token}/"
    updater.bot.set_webhook(url)
    logging.warning(f"IN RUN BOT - {url}")

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Это Mycar Reply Bot. \n" \
                                  f"Для начала работы добавьте свой токен с помощью команды /bind_token $token \n" \
                                  f"Например: /bind_token 65be537f-80cc-4c9e-ab95-2b7eca01186a")
    logging.warning(f"{update.effective_chat.id}")

def bind_token(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="В этой команде необходимо обязательно передать ваш токен")
    token = context.args[0]

    try:
        token = uuid.UUID(token)
        user = MainUser.objects.get(access_token=token)
    except MainUser.DoesNotExist:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Данный токен не зарегистрирован")
    except (ValidationError, ValueError) as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Это невалидный токен")
    else:
        user.telegram_chat_id = update.effective_chat.id
        user.save()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Ваш токен успешно зарегистрирован, {user.first_name}")

def send_message(chat_id, message):
    CallbackContext(dispatcher).bot.send_message(chat_id=chat_id,
                                                 text=message)

start_handler = CommandHandler('start', start)
bind_token_handler = CommandHandler('bind_token', bind_token)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(bind_token_handler)
