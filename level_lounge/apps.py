from django.apps import AppConfig


class LevelLoungeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'level_lounge'

    def ready(self):
        import your_app_name.signals  # Ensure the signals are connected
