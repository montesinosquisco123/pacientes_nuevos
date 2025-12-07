from pathlib import Path

# =====================
# BASE
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================
# SEGURIDAD (SOLO DESARROLLO)
# =====================
SECRET_KEY = 'django-insecure-1234567890'
DEBUG = True
ALLOWED_HOSTS = []

# =====================
# APLICACIONES
# =====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'clinica',
]

# =====================
# MIDDLEWARE
# =====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =====================
# URLS
# =====================
ROOT_URLCONF = 'pacientes_nuevos.urls'

# =====================
# TEMPLATES
# =====================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# =====================
# WSGI
# =====================
WSGI_APPLICATION = 'pacientes_nuevos.wsgi.application'

# =====================
# BASE DE DATOS
# =====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'pacientes_nuevos.sqlite3',
    }
}

# =====================
# VALIDACIÓN DE CONTRASEÑAS
# =====================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =====================
# IDIOMA Y ZONA HORARIA
# =====================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# =====================
# ARCHIVOS ESTÁTICOS
# =====================
STATIC_URL = 'static/'

# =====================
# DEFAULT
# =====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
