from django.apps import AppConfig
from django.contrib.auth import get_user_model


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        def get_profile(user):
            return user.profiles.filter(primary_profile=True).first()

        def has_profile(user):
            return user.profiles.filter(primary_profile=True).count() > 0

        def get_children(user):
            return user.profiles.filter(primary_profile=False)

        def get_name(user):
            profile = get_profile(user)
            if profile is not None:
                return profile.get_full_name()

            return user.username

        get_user_model().add_to_class('get_profile', get_profile)
        get_user_model().add_to_class('has_profile', has_profile)
        get_user_model().add_to_class('get_children', get_children)
        get_user_model().add_to_class('__str__', get_name)
