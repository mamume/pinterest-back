from typing import ContextManager
from rest_framework import serializers
from account.models import UserProfile, UserFollowing
from operator import itemgetter
from pprint import pprint


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'full_name', 'profile_pic',
                  'username', 'bio', 'following_count', 'followers_count']

    full_name = serializers.SerializerMethodField('get_full_name')
    following_count = serializers.SerializerMethodField('get_following_count')
    followers_count = serializers.SerializerMethodField('get_followers_count')

    def get_full_name(self, instance: UserProfile):
        return f"{instance.first_name} {instance.last_name}"

    def get_following_count(self, instance: UserProfile):
        return UserFollowing.objects.filter(user=instance).count()

    def get_followers_count(self, instance: UserProfile):
        return UserFollowing.objects.filter(followed_user=instance).count()


class UserFollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['follower', ]

    follower = serializers.SerializerMethodField('get_follower')

    def get_follower(self, instance: UserFollowing):
        serializer_context = {'request': self.context.get('request')}
        followers = UserProfile.objects.filter(pk=instance.user.id)

        return FollowerData(followers, many=True, context=serializer_context).data


class UserFolloweingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['following', ]

    following = serializers.SerializerMethodField('get_following')

    def get_following(self, instance: UserFollowing):
        serializer_context = {'request': self.context.get('request')}
        following = UserProfile.objects.filter(pk=instance.followed_user.id)

        return FollowerData(following, many=True, context=serializer_context).data


class FollowerData(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'full_name', 'profile_pic']

    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, instance: UserProfile):
        return f"{instance.first_name} {instance.last_name}"
