from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article


# Create your views here.


def index(request):
    return HttpResponse(Article.objects.all())


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article
    }

    return render(request, 'blog/detail.html', context)
