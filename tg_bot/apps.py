from django.apps import AppConfig


class TGBotConfig(AppConfig):
    name = 'tg_bot'

    def ready(self):
        from .utils import run_bot

        run_bot()