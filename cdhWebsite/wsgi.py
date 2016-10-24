"""
WSGI config for demoSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/var/www/cdhProd/')
sys.path.append('/var/www/venv/lib64/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

import pymysql
pymysql.install_as_MySQLdb()

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("cdhWebsite"))

application = get_wsgi_application()
