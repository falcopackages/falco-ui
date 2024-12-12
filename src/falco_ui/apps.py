from django.apps import AppConfig


class FalcoUIConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "falco_ui"

    # def ready(self):
    #     from django.conf import settings
    #
    #     settings.TAILWIND_CLI_SRC_REPO = "dobicinaitis/tailwind-cli-extra"
    #     settings.TAILWIND_CLI_ASSET_NAME = "tailwindcss-extra"
    #     settings.TAILWIND_CLI_VERSION = "1.7.19"
