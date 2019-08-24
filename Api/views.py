from Blog.models import Article
from rest_framework import viewsets, permissions, authentication
from .serializers import ArticleSerializer

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.AllowAny,)
