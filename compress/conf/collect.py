"""
Autodiscover per-application compress_settings
"""
from importlib import import_module
from django.conf import settings

def autodiscover():
    for app in settings.INSTALLED_APPS:
        try:
            import_module(app)
            settings_compress = import_module('.settings_compress', app)
            compress_css, compress_js = getattr(settings_compress, 'COMPRESS_CSS', {}), getattr(settings_compress, 'COMPRESS_JS', {})
            yield compress_css, compress_js
        except ImportError:
            continue
