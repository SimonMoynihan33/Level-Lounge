from django.apps import AppConfig


class LevelLoungeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'level_lounge'

    def ready(self):
        import level_lounge.signals  # Ensure the signals are connected
