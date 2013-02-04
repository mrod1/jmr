#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jmr.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uccsc.settings")
>>>>>>> 1e50d6a3559765e6591af3cb87d088c43b22462c

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
