from rest_framework import serializers
from .models import Follower
from web.user_profile.serializers import UserByFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber',)

