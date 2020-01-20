"""
Django settings for ops_notfiy project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'soi@kc4g08u!=8mxh%wg6htcnl43+t!8(@i$nf)rl5ff6@&-y7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'log_mail'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ops_notfiy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ops_notfiy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST') if "EMAIL_HOST" in os.environ else 'smtp.exmail.qq.com'
EMAIL_PORT = os.getenv('EMAIL_PORT') if "EMAIL_PORT" in os.environ else 465
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER") if "EMAIL_HOST_USER" in os.environ else 'devops@isyscore.com'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD") if "EMAIL_HOST_PASSWORD" in os.environ else '6KQKxrtL@E8FpkJ'
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL") if "EMAIL_USE_SSL" in os.environ else True
EMAIL_FROM = os.getenv("EMAIL_FROM") if "EMAIL_FROM" in os.environ else 'devops@isyscore.com'
KIBANA_URL = os.getenv("KIBANA_URL") if "KIBANA_URL" in os.environ else 'http://10.30.30.25:15601'
KIBANA_DATE_TIME = os.getenv("KIBANA_DATE_TIME") if "KIBANA_DATE_TIME" in os.environ else 'now-10m'


EMAIL_TO = {
	"[iscshow-run-service]": {
		"username": "应健健",
		"mailto": ["yingjj@isyscore.com"]
	},
	"other": {
		"username": "ops",
		"mailto": ["devops@isyscore.com"]
	}
}
#kibana url


#promethues notfiy
PRO_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=20de74df-fdcf-4a56-a410-990155f9bfe2"
PRO_PROJECT = "益展大厦"