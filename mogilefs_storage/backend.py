import urlparse
from django.conf import settings
from django.core.files.storage import Storage
from django.core.exceptions import ImproperlyConfigured
import pymogile

class MogileFSStorage(Storage):
    """MogileFS filesystem storage"""

    mogile_class = None

    def __init__(self, base_url=settings.MEDIA_URL):
        # the MOGILEFS_MEDIA_URL overrides MEDIA_URL
        if hasattr(settings, 'MOGILEFS_MEDIA_URL'):
            self.base_url = settings.MOGILEFS_MEDIA_URL
        else:
            self.base_url = base_url

        for var in ('MOGILEFS_TRACKERS', 'MOGILEFS_DOMAIN',):
            if not hasattr(settings, var):
                raise ImproperlyConfigured, "You must define %s to use the MogileFS backend." % var

        self.trackers = settings.MOGILEFS_TRACKERS
        self.domain = settings.MOGILEFS_DOMAIN
        self.client = pymogile.Client(domain=self.domain, trackers=self.trackers)

    def _open(self, name, mode):
        return self.client.read_file(name)


    def url(self, name):
        return urlparse.urljoin(self.base_url, name).replace('\\', '/')


    def exists(self, name):
        return bool(self.client.get_paths(name))


    def _save(self, name, content):
        self.client.store_file(name, content, cls=self.mogile_class)

    def delete(self, name):
        self.client.delete(name)


