__version__ = '0.6.0'


import django
from distutils.version import StrictVersion
dj_version = django.get_version()

if StrictVersion(dj_version) < StrictVersion('1.7'):
    from rolepermissions.loader import load_roles_and_permissions
    load_roles_and_permissions()
