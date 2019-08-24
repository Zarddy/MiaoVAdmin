from Blog.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['uid', 'title', 'cover', 'content', 'video_url', 'published_time']
