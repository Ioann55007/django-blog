from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet, GenericViewSet
from . import serializers
from .models import Follower
from .serializers import ListFollowerSerializer
from main.pagination import BasePageNumberPagination

class ListFollowerViewSet(ViewSet):
    """Вывод списка подписчиков пользователя"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(users=self.request.user)


class FollowerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    """Добавление в подписчики"""
    pagination_class = BasePageNumberPagination
    # queryset = Follower.objects.all()
    http_method_names = ('get', 'post')
    serializer_class = serializers.ToUserSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ListFollowerSerializer
        elif self.action == 'create':
            return serializers.CreateSubscriptionSerializer
        elif self.action == 'user_followers' or self.action == 'user_following':
            return serializers.UserByFollowerSerializer

    def get_queryset(self):
        if self.action == 'user_followers':
            return self.request.user.followers.all()
        elif self.action == 'user_following':
            return self.request.user.following.all()

    def user_followers(self, request):
        return self.list(request)

    def user_following(self, request):
        return self.list(request)
