from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from blog.choices import ArticleStatus

User = get_user_model()


class UserProfileService:

    @staticmethod
    def get_user_profile(user_id: int):
        user_articles = Count('article_set', filter=Q(article_set__status=ArticleStatus.ACTIVE))
        # user_likes = Count('likes')
        return (
            User.objects.select_related('profile')
            .annotate(user_posts=user_articles)
            .get(id=user_id)
        )

    @staticmethod
    def user_queryset():
        return User.objects.exclude(is_active=False).select_related('profile')
