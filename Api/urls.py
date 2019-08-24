from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from Api import views


router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet, base_name="articles")


app_name = 'api_rest_framework'
urlpatterns = [
    # ex: /api/
    url(r'^', include(router.urls))
]