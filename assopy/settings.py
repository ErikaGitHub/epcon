# -*- coding: UTF-8 -*-
from django.conf import settings

if hasattr(settings, 'ASSOPY_JANRAIN'):
    JANRAIN = {
        'domain': settings.ASSOPY_JANRAIN['domain'],
        'app_id': settings.ASSOPY_JANRAIN['app_id'],
        'secret': settings.ASSOPY_JANRAIN['secret'],
    }
else:
    JANRAIN = None
