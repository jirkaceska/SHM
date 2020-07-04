from django.apps import AppConfig
from django.contrib.auth import get_user_model


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        def get_profile(user):
            return user.profiles.filter(primary_profile=True).first()

        def has_profile(user):
            return user.profiles.filter(primary_profile=True).count() > 0

        get_user_model().add_to_class('get_profile', get_profile)
        get_user_model().add_to_class('has_profile', has_profile)
