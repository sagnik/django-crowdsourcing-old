#!/usr/bin/env python
import os, sys

from django.core.management import execute_manager

# to be able to import the crowdsourcing app

if __name__ == "__main__":
 os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_app.settings")
 from django.core.management import execute_from_command_line
 execute_from_command_line(sys.argv)
