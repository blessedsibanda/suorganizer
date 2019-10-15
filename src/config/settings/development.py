from .base import *

DEBUG = ENV.bool('DEBUG', default=True)

TEMPLATES[0]['OPTIONS'].update(
    {
        'debug': ENV.bool(
            'TEMPLATE_DEBUG', default=True
        )
    }
)