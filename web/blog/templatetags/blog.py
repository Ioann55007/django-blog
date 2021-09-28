from django import template
from django.db.models import Count

from blog.models import Category, ArticleTag
from blog.serializers import CategorySerializer

from blog.models import Article, TaggedArticle

register = template.Library()


@register.simple_tag(name='categories')
def categories_list(limit: int = 99):
    queryset = Category.objects.all()[:limit]
    serializer = CategorySerializer(queryset, many=True)
    return serializer.data



@register.simple_tag()
def popular_tags_list():
    tags = ArticleTag.objects.annotate(num_tags=Count('tagged_article')).order_by('-num_tags')
    return tags
