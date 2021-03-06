from django.apps import AppConfig


class ClinicsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clinics'
    verbose_name = "Клиники"

    def ready(self):
        import apps.clinics.signals
