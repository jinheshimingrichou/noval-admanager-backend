from django.urls import path

from game import views

urlpatterns = [
    path('page/index', views.IndexPageView.as_view()),
    path('page/sitemap', views.SitemapPageView.as_view())
]
