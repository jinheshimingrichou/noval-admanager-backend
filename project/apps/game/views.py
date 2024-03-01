from datetime import datetime, timezone

from django.conf import settings
from django.db.models import Q, Count, Case, When
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_extensions.cache.decorators import cache_response

from utils.response import APIResponse
from utils.pagination import APIPageNumberPagination

from game import models as game_models
from game import serializers as game_serializers


class IndexPageView(APIView):
    def cache_key(self, view_instance, view_method, request, args, kwargs):
        return f'backend:game:index'

    @cache_response(timeout=settings.CACHE_TIME_INDEX, key_func='cache_key')
    def get(self, request):
        game_objs = game_models.Game.objects.all()
        index_game_list = game_serializers.GameSimpleSerializer(instance=game_objs, many=True).data
        data = {
            'index_game_list': index_game_list
        }
        return APIResponse(data=data, status=status.HTTP_200_OK)


class SitemapPageView(APIView):
    def get(self, request):
        sitemap = [
            {
                'url': '/',
                'changefreq': 'weekly',
                'priority': 1,
                'lastmod': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')
            }
        ]
        return Response(sitemap)
