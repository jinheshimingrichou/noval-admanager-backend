from datetime import datetime

from django.db import models

from utils.models import TimeBaseModel


class Game(TimeBaseModel):
    id = models.BigAutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=200, default='')
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        app_label = 'game'
        db_table = 'game_game'
