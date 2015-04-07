#!/usr/bin/env python
import os
import sys
# YAY HERE IS NEW TEXT
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "buylocalartor.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
