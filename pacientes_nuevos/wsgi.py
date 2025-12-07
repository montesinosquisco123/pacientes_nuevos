import os
import sys

path = '/home/tuusuario/pacientes_nuevos'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pacientes_nuevos.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
