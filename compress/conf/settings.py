from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from collect import autodiscover


COMPRESS_ROOT = getattr(settings, 'COMPRESS_ROOT', settings.MEDIA_ROOT)
COMPRESS_URL = getattr(settings, 'COMPRESS_URL', settings.MEDIA_URL)

COMPRESS = getattr(settings, 'COMPRESS', not settings.DEBUG)
COMPRESS_AUTO = getattr(settings, 'COMPRESS_AUTO', True)
COMPRESS_VERSION = getattr(settings, 'COMPRESS_VERSION', False)
COMPRESS_VERSION_PLACEHOLDER = getattr(settings, 'COMPRESS_VERSION_PLACEHOLDER', '?')
COMPRESS_VERSION_DEFAULT = getattr(settings, 'COMPRESS_VERSION_DEFAULT', '0')
COMPRESS_VERSIONING = getattr(settings, 'COMPRESS_VERSIONING', 'compress.versioning.mtime.MTimeVersioning')

COMPRESS_CSS_FILTERS = getattr(settings, 'COMPRESS_CSS_FILTERS', ['compress.filters.csstidy.CSSTidyFilter'])
COMPRESS_JS_FILTERS = getattr(settings, 'COMPRESS_JS_FILTERS', ['compress.filters.jsmin.JSMinFilter'])

COMPRESS_CSS, COMPRESS_JS = {}, {}
for compress_css, compress_js in autodiscover():
    COMPRESS_CSS.update(compress_css)
    COMPRESS_JS.update(compress_js)
COMPRESS_CSS.update(getattr(settings, 'COMPRESS_CSS', {}))
COMPRESS_JS.update(getattr(settings, 'COMPRESS_JS', {}))

if COMPRESS_CSS_FILTERS is None:
    COMPRESS_CSS_FILTERS = []

if COMPRESS_JS_FILTERS is None:
    COMPRESS_JS_FILTERS = []
