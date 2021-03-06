import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# from .additional_settings.defender_settings import *
from .additional_settings.swagger_settings import *
# from .additional_settings.cacheops_settings import *
from .additional_settings.logging_settings import *
from .additional_settings.celery_settings import *
from .additional_settings.allauth_settings import *
from .additional_settings.jwt_settings import *
from .additional_settings.summernote_settings import *
from .additional_settings.smtp_settings import *


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "hjzjhzl;hjzlhjzhjzhjzkhljzkkothjzodtjhdaipjhopzjzlkbmbmbmznmznmznmzjnzoitjn")

DEBUG = int(os.environ.get("DEBUG", default=1))
FRONTEND_SIRE = 'http://localhost:8000'
X_FRAME_OPTIONS = "SAMESITE"
ALLOWED_HOSTS: list = os.environ.get("DJANGO_ALLOWED_HOSTS", 'localhost,127.0.0.1').split(",")
AUTH_USER_MODEL = 'main.User'

SUPERUSER_EMAIL = os.environ.get('SUPERUSER_EMAIL', 'test@test.com')
SUPERUSER_PASSWORD = os.environ.get('SUPERUSER_PASSWORD', 'tester26')

MICROSERVICE_TITLE = os.environ.get('MICROSERVICE_TITLE', 'Template')
GITHUB_URL = os.environ.get('GITHUB_URL', 'https://github.com')

REDIS_URL = os.environ.get('REDIS_URL')

USE_HTTPS = int(os.environ.get('USE_HTTPS', 0))
ENABLE_SENTRY = int(os.environ.get('ENABLE_SENTRY', 0))
ENABLE_SILK = int(os.environ.get('ENABLE_SILK', 0))
ENABLE_DEBUG_TOOLBAR = int(os.environ.get('ENABLE_DEBUG_TOOLBAR', 0))
ENABLE_RENDERING = int(os.environ.get('ENABLE_RENDERING', 1))

INTERNAL_IPS = []

ADMIN_URL = os.environ.get('ADMIN_URL', 'admin')

SWAGGER_URL = os.environ.get('SWAGGER_URL')

API_KEY_HEADER = os.environ.get('API_KEY_HEADER')
API_KEY = os.environ.get('API_KEY')

HEALTH_CHECK_URL = os.environ.get('HEALTH_CHECK_URL')
SITE_ID = 1

USER_AVATAR_MAX_SIZE = 4.0

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = [
    'user_profile.apps.UserProfileConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

]

THIRD_PARTY_APPS = [
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework_simplejwt.token_blacklist',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'rosetta',
    'django_summernote',

]

LOCAL_APPS = [
    'main.apps.MainConfig',
    'auth_app.apps.AuthAppConfig',
    'blog.apps.BlogConfig',
    'contact_us.apps.ContactUsConfig',
    'actions.apps.ActionsConfig',

]

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'main.middleware.HealthCheckMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'defender.middleware.FailedLoginMiddleware',
    'django.middleware.locale.LocaleMiddleware',

]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'microservice_request.permissions.HasApiKeyOrIsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

if ENABLE_RENDERING:
    """ For build CMS using DRF """
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    )


ROOT_URLCONF = 'src.urls'

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'
ASGI_APPLICATION = 'src.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://redis:6379/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#
#         }
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TZ', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIMEZONE_COOKIE_NAME = 'timezone'
TIMEZONE_COOKIE_AGE = 15552000  # 60*60*24*180

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('en', _('English')),
)

ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = LANGUAGE_CODE
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'English'
ROSETTA_SHOW_AT_ADMIN_PANEL = True
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = False


if JAEGER_AGENT_HOST := os.environ.get('JAEGER_AGENT_HOST'):
    from jaeger_client import Config
    from jaeger_client.config import DEFAULT_REPORTING_PORT
    from django_opentracing import DjangoTracing
    """If you don't need to trace all requests, comment middleware and set OPENTRACING_TRACE_ALL = False
        More information https://github.com/opentracing-contrib/python-django/#tracing-individual-requests
    """
    MIDDLEWARE.insert(0, 'django_opentracing.OpenTracingMiddleware')
    OPENTRACING_TRACE_ALL = True
    tracer = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "local_agent": {
                "reporting_port": os.environ.get("JAEGER_AGENT_PORT", DEFAULT_REPORTING_PORT),
                "reporting_host": JAEGER_AGENT_HOST,
            },
            "logging": int(os.environ.get('JAEGER_LOGGING', False)),
        },
        service_name=MICROSERVICE_TITLE,
        validate=True,
    ).initialize_tracer()
    OPENTRACING_TRACING = DjangoTracing(tracer)

if (SENTRY_DSN := os.environ.get('SENTRY_DSN')) and ENABLE_SENTRY:
    # More information on site https://sentry.io/
    from sentry_sdk import init
    from sentry_sdk.integrations.django import DjangoIntegration
    init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
