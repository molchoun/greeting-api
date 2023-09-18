"""Common settings for Announcements"""


def plugin_settings(settings):
    settings.FEATURES['ENABLE_GREETING_API'] = True
    settings.REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'edx_rest_framework_extensions.auth.jwt.authentication.JwtAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    }
