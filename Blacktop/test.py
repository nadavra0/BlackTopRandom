import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Blacktop.settings')

import django
django.setup()

from players.models import Player



user =Player(name="John", pos="PG")
user.save()