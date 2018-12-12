
import os
import sys
sys.path = ['/var/www/newapp'] + sys.path

from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE']= 'newapp.settings'
application = get_wsgi_application()



