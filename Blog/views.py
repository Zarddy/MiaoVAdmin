from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article


# Create your views here.


def index(request):
    articles = get_list_or_404(Article)

    return render(request, 'blog/index.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    return render(request, 'blog/detail.html', {'article': article})
