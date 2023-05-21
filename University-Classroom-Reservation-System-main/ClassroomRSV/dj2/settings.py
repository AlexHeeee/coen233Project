
import os
from util.configread import config_read


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'w5yn#0gn2tt7pvu%hvwt0!lt=!$6+eqp4%m8)u3u#gknm@jm)k'
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
    "main",
]


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_COOKIE_NAME  = "sessionid"
SESSION_COOKIE_PATH  = "/"
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = False

ROOT_URLCONF = 'dj2.urls'
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'dj2.wsgi.application'

dbtype, host, port, user, passwd, dbName, charset = config_read("config.ini")
dbName=dbName.replace(" ","").strip()
print(dbtype, host, port, user, passwd, dbName, charset)

if dbtype == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'sql_mode': 'traditional',
                'init_command': "SET sql_mode='traditional'",
            },
            'NAME': dbName,
            'USER': user,
            'PASSWORD': passwd,
            'HOST': host,
            'PORT': port,
            'charset': charset,
            'TEST': {
                'CHARSET': charset,
                'COLLATION': 'utf8_general_ci',
            },
            'CONN_MAX_AGE':60
        },
    }
else:
    print("please use mysql5.5 or higher version database")
    os._exit(1)

# Password validation

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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/assets/'
STATICFILES_DIRS =[
os.path.join(BASE_DIR, "templates/front/assets"),
]

# media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if os.path.isdir(MEDIA_ROOT) == False:
    os.mkdir(MEDIA_ROOT)