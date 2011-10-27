import os
import os.path
import tempfile

def _ensure_path(path):
    try:
        os.makedirs(path)
    except (IOError, OSError,):
        if not os.path.isdir(path):
            raise

TEMP_ROOT = os.path.join(tempfile.gettempdir(), 'django-processedfilefield-test')
_ensure_path(TEMP_ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TEMP_ROOT, 'db.sqlite'),
    }
}

INSTALLED_APPS = (
    'testproject.testapp',
)

MEDIA_ROOT = os.path.join(TEMP_ROOT, 'media')
_ensure_path(MEDIA_ROOT)