
from django import template
from django.db.models import Count, Sum, Q
from blog.choices import ArticleStatus
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

    tags = ArticleTag.objects.annotate(
        num_tags=Count('tagged_article', filter=Q(
            tagged_article__content_object__status=ArticleStatus.ACTIVE))
    ).order_by('-num_tags')[0:8]
    return tags


@register.inclusion_tag('blog/popular_posts.html')
def popular_posts_list(cnt=7):
    articles = Article.objects.order_by('-views')[:cnt]
    return {"posts": articles}
