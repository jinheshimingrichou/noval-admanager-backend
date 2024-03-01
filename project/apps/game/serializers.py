from datetime import datetime

from django.conf import settings
from rest_framework import serializers

from utils.imgproxy import ImgProxy, ImgProxyOptions

from game import models as game_models


class GameSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = game_models.Game
        fields = ('id', 'name', 'slug')
