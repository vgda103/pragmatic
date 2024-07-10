"""
Django settings for pragmatic project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from django.urls import reverse_lazy
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(
    env_file= os.path.join( BASE_DIR, '.env' )
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-=c5ge!bti_vqhkqjr-3ii=b95ws9m9#nw6@r4p_ebz(^ezxm*g'
SECRET_KEY = env( 'SECRET_KEY' )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 38. 모바일 디버깅 - 수정
# 기존
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accountapp',
    'bootstrap5',
    'profileapp',
    'articleapp',
    'commentapp',
    'projectapp', 
    'subscribeapp', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pragmatic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join( BASE_DIR, 'template' ) ],
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

WSGI_APPLICATION = 'pragmatic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 11강. CSS
# stitic 폴더 경로를 만든다
STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )

# 폴더 명시
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 로그인 / 아웃 다시접속 주소 설정
# 45강 프로젝트 마무리 - 수정
# LOGIN_REDIRECT_URL = reverse_lazy( 'accountapp:hello_world' ) - 기존
LOGIN_REDIRECT_URL = reverse_lazy( 'home' )
LOGOUT_REDIRECT_URL = reverse_lazy( 'accountapp:login' )
LOGIN_URL = 'accountapp:login'

# 29강 슈퍼계정, 미디어 설정

# 11강. CSS
# 미디어 설정
# 주소창에서 접근할때 /media/ 이하의 경로로 접근할때 실제 media 파일에 접근 할수 있다.
MEDIA_URL = '/media/'
# 미디어 파일을 서버에 올렸을때 어느 경로에 지정될것인지에 대한 경로
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
