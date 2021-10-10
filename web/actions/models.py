from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follower(models.Model):
    """Модель подписчиков"""

    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_from')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_to')
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        unique_together = ('subscriber', 'to_user')
