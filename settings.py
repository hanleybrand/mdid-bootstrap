from os.path import normpath, join
from django.conf import settings
from config.settings import ROOIBOS_ROOT

MDID_BOOTSTRAP = True

MASTER_TEMPLATE = 'bootstrap-master.html'

# temp_dirs = list(settings.TEMPLATE_DIRS)
#
# temp_dirs.insert(normpath(join(ROOIBOS_ROOT, 'apps', 'mdid-bootstrap', 'templates')),0)
TEMPLATE_DIRS = (
    normpath(join(ROOIBOS_ROOT, 'apps', 'mdid-bootstrap', 'templates')),
)

