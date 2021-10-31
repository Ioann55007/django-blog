from django.db.models import TextChoices
from django.forms import CharField
from django.db import models


class FollowerStatus(TextChoices):
    FOLLOW = ('Follow', 'Follow')
    UNFOLLOW = ('Unfollow', 'Unfollow')
