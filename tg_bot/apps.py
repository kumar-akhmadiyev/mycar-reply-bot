from django.apps import AppConfig


class TGBotConfig(AppConfig):
    name = 'tg_bot'

    def ready(self):
        from django.conf import settings
        from tg_bot.utils import run_bot

        if not settings.TESTING:
            run_bot()
