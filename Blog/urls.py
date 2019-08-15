from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/detail/5
    path('detail/<int:article_id>/', views.detail, name='detail'),
]
