"""
greeting_api Django application initialization.
"""

from django.apps import AppConfig


class GreetingApiConfig(AppConfig):
    """
    Configuration for the greeting_api Django application.
    """

    name = 'greeting_api'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'greeting_api',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings'},
            }
        },
    }
