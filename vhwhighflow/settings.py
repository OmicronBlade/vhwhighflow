import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_y#p+#emw$=6ff(3*d1akb)stxn00smzy8qo2r&wu66jx)y)n1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','.herokuapp.com']

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')
STATIC_URL = '/static/'


# Application definition

INSTALLED_APPS = [
    'vhwhighflow',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'vhwhighflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'vhwhighflow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
#VHWFlow!

try:
    import dj_database_url

    ON_HEROKU = True

    if 'RDS_DB_NAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAMEIN'],
                'PORT': os.environ['RDS_PORT']
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.config(default='sqlite:///' + BASE_DIR + '/db.sqlite3')
        }

except ImportError:
    if 'RDS_DB_NAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAMEIN'],
                'PORT': os.environ['RDS_PORT']
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': ''
            }
        }



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'Africa/Johannesburg'
USE_I18N = True
USE_L10N = False
USE_TZ = True

#Date formatting
DATE_INPUT_FORMATS = ['%d/%m/%Y', '%d/%m/%y']

DATE_FORMAT = 'd/m/Y'
#
#DATETIME_INPUT_FORMAT = [
#    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
#    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
#    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
#    '%Y-%m-%d',              # '2006-10-25'
#    '%d/%m/%Y %H:%M:%S',     # '25/10/2006 14:30:59'
#    '%d/%m/%Y %H:%M:%S.%f',  # '25/10/2006 14:30:59.000200'
#    '%d/%m/%Y %H:%M',        # '25/10/2006 14:30'
#    '%d/%m/%Y'               # '25/10/2006'
#]
