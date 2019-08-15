from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Article


# Create your views here.


def index(request):
    return HttpResponse(Article.objects.all())


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)

    return HttpResponse('Article is %s ' % article)
