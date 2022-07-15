from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework import viewsets
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    class Meta:
        model = Article
        fields = '__all__'
