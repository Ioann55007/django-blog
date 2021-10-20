from datetime import datetime

import redis
from django import template
from django.core.cache import cache
from django.db.models import Count, Sum, Q
from django_redis import get_redis_connection
from future.backports.datetime import timedelta
from rest_framework import request

from blog.choices import ArticleStatus
from blog.models import Category, ArticleTag
from blog.serializers import CategorySerializer
from blog.models import Article, TaggedArticle
from src import settings

register = template.Library()


@register.simple_tag(name='categories')
def categories_list(limit: int = 99):
    queryset = Category.objects.all()[:limit]
    serializer = CategorySerializer(queryset, many=True)
    return serializer.data


@register.simple_tag()
def popular_tags_list():
    cache_key = 'popular_tags_list'
    if cache_key in cache:
        print('in cache')
        return cache.get(cache_key)
    tags = ArticleTag.objects.annotate(
        num_tags=Count('tagged_article', filter=Q(
            tagged_article__content_object__status=ArticleStatus.ACTIVE))
    ).order_by('-num_tags')[0:8]
    cache.set(cache_key, list(tags), timeout=40)
    print('out_cache')
    return tags


#
# @register.inclusion_tag('blog/includes/sidebar_blocks/popular_posts.html')
# def popular_posts_list(cnt=7):
#     articles = Article.objects.order_by('-title')[:cnt]
#
#     def current_key():
#         return datetime.now().strftime('%H:%M')
#
#     def set_to_key(user_id):
#         if request.user.is_authenticated():
#            key = current_key()
#            get_redis_connection("default").sadd(key, user_id)
#
#     def get_online():
#         now = datetime.now()
#         interval = [now - timedelta(minutes=x) for x in range(100)]
#         interval = [i.strftime('%H:%M') for i in interval]
#         try:
#             online = len(get_redis_connection("default").sunion(interval))
#         except:
#             online = 1
#         return int(online)
#
#     return {"posts": articles}


@register.inclusion_tag('blog/includes/sidebar_blocks/popular_posts.html')
def popular_posts_list(cnt=7):
    articles = Article.objects.order_by('-title')[:cnt]
    current_key = datetime.now().strftime('%H:%M')

    def gt(user_id):
        if request.user.is_authenticated():
            key = current_key
            get_redis_connection("default").sadd(key, user_id)
            now = datetime.now()
            interval = [now - timedelta(minutes=x) for x in range(100)]
            interval = [i.strftime('%H:%M') for i in interval]
            try:
                online = len(get_redis_connection("default").sunion(interval))
            except:
                online = 1
            return int(online)
    return {"posts": articles}
