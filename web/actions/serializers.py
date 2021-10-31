from django.db.models import TextChoices, Q
from rest_framework import serializers, response, request
from .models import Follower, User
from user_profile.serializers import UserByFollowerSerializer
from .choises import FollowerStatus
from django.db import models


class ListFollowerSerializer(serializers.ModelSerializer):
    subscriber = UserByFollowerSerializer(many=True, read_only=True)
    to_user = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber', 'to_user')


class ToUserSerializer(ListFollowerSerializer):
    """Подписка на пользователя"""
    # permission_classes = [permissions.IsAuthenticated]
    to_user = serializers.SerializerMethodField('get_post_subscription')

    def get_post_subscription(self, pk):
        to_user = User.objects.filter(id=pk)
        if to_user.exists():
            Follower.objects.create(subscriber=request.user, user=to_user)
            return response.Response(status=201)
        return response.Response(status=404)


class CreateSubscriptionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(min_value=1)

    def save(self):

        subscriber = self.context['request'].user
        to_user: int = self.validated_data['user_id']

        print(subscriber, to_user)

        if not Follower.objects.filter(subscriber=subscriber, to_user_id=to_user).exists():

            """Пользователь не подписан, подписать"""
            self.follower_status = FollowerStatus.UNFOLLOW
            Follower.objects.create(
                subscriber=subscriber,
                to_user_id=to_user,

            )

        else:
            """Пользователь уже подписан, нужно удалить подписку"""
            self.follower_status = FollowerStatus.FOLLOW
            Follower.objects.filter(
                to_user_id=to_user).delete()

    @property
    def data(self):
        return {'follower_status': self.follower_status}

