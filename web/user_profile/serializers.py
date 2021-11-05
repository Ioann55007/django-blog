from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework import serializers
from actions.models import Follower
from actions.choises import FollowerStatus
from .models import Profile
from .choices import GenderChoice

User = get_user_model()


class ShortUserSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(source='profile.avatar')
    url = serializers.URLField(source='get_absolute_url')

    class Meta:
        model = User
        fields = ('id', 'full_name', 'avatar', 'url')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('birthday', 'avatar', 'gender',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'first_name', 'last_name', 'email', 'profile', 'is_active', 'email_verified',
            'phone_number', 'user_posts',
        )
        read_only_fields = ('full_name', 'email_verified', 'user_posts')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update(rep.pop('profile'))
        return rep


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar',)

    def validate_avatar(self, avatar):
        if avatar.size > settings.USER_AVATAR_MAX_SIZE * 1024 * 1024:
            raise serializers.ValidationError(_("Max size is {size} MB".format(size=settings.USER_AVATAR_MAX_SIZE)))
        return avatar

    def save(self, *args, **kwargs):
        if self.instance.avatar and not self.instance.is_default_image():
            self.instance.set_image_to_default()
        return super().save(**kwargs)


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(source='profile.birthday')
    gender = serializers.ChoiceField(source='profile.gender', choices=GenderChoice.choices)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'birthday', 'gender')


class UserListSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    follower_status = serializers.SerializerMethodField('get_follower_status')

    def get_follower_status(self, obj):
        current_user = self.context['request'].user

        if Follower.objects.filter(subscriber=current_user, to_user=obj).exists():
            return FollowerStatus.UNFOLLOW
        return FollowerStatus.FOLLOW

    class Meta:
        model = User
        fields = ('id', 'full_name', 'avatar', 'follower_status')


class UserByFollowerSerializer(serializers.ModelSerializer):
    """сериализация подписчиков"""

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
