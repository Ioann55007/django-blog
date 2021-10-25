from django.db.models import TextChoices


class FollowerStatus(TextChoices):
    FOLLOW = ('Follow', 'Follow')
    UNFOLLOW = ('Unfollow', 'Unfollow')
