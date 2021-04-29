import logging.config

from flask import Flask


class _InfoFilter(logging.Filter):

    def filter(self, record):
        return record.levelno < logging.WARNING


def setup_logging(app: Flask):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'info_filter': {
                '()': _InfoFilter
            }
        },
        'formatters': {
            'default': {
                'format': app.config.get('LOG_FORMAT'),
                'datefmt': app.config.get('LOG_DATEFMT')
            }
        },
        'handlers': {
            'console_stdout': {
                'level': app.config.get('LOG_LEVEL'),
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout',
                'filters': ['info_filter'],
            },
            'console_stderr': {
                'level': logging.WARNING,
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            }
        },
        'loggers': {
            '': {
                'level': app.config.get('LOG_LEVEL'),
                'handlers': ['console_stdout', 'console_stderr'],
            },
        },
    })
