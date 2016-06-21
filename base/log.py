# -*- coding: utf-8 -*-

import logging
import logging.config

logger = logging.getLogger()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'old': {
            'format': '%(asctime)s [%(levelname)7s] -- %(message)s (%(filename)s:%(lineno)s)'
        },
        'standard': {
            'format': '%(asctime)s %(levelname)7s (%(filename)16s:%(lineno)4s): %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'log/log.plog',
            'mode': 'a',
            # 'maxBytes': 10485760,
            # 'backupCount': 1,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'propagate': False,
            'level': 'DEBUG'
        }
    }
})


class ConsoleExceptionLoggerMiddleware(object):
    def process_exception(self, request, exception):
        import traceback
        import sys
        exc_info = sys.exc_info()
        print("-" * 30 + "Exception" + "-" * 50)
        print('\n'.join(
            traceback.format_exception(*(exc_info or sys.exc_info()))))
        print("-" * 88)
