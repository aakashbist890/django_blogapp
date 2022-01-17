from django.apps import AppConfig


class RegistrationappConfig(AppConfig):
    name = 'registrationapp'

    def ready(self):
        import registrationapp.signals
