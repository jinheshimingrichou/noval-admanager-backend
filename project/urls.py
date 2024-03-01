"""
项目主路由

eg:
    /api/v1/noval/page/index
    /api/v1/noval/page/detail
    /api/v1/noval/page/play
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django 后台
    path('novaladmin/', admin.site.urls),
    # 管理 API
    path('api/v1/system/', include('system.urls')),

]
