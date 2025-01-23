#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    dev_mode = input('what development mode are you on?: dev or prod: ')
    if dev_mode == 'dev':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kyd_finance.settings.dev')
    elif dev_mode == 'prod':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kyd_finance.settings.prod')

    else:
        print('Choose a development mode')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
