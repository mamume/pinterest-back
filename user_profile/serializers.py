from rest_framework import serializers
from account.models import UserProfile, UserFollowing
from pin.api.v1.serializers import PinSerializer
from pin.models import Pin
from board.models import Board
from board.serializers import BoardSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'full_name', 'profile_pic',
                  'username', 'bio', 'following_count', 'followers_count', 'pins', 'boards']

    full_name = serializers.SerializerMethodField('get_full_name')
    following_count = serializers.SerializerMethodField('get_following_count')
    followers_count = serializers.SerializerMethodField('get_followers_count')
    pins = serializers.SerializerMethodField('get_pins')
    boards = serializers.SerializerMethodField('get_boards')

    def get_boards(self, instance: UserProfile):
        serializer_context = {'request': self.context.get('request')}
        boards = Board.objects.filter(owner=instance)
        return BoardSerializer(boards, many=True, context=serializer_context).data

    def get_pins(self, instance: UserProfile):
        serializer_context = {'request': self.context.get('request')}
        pins = Pin.objects.filter(owner=instance)
        return PinSerializer(pins, many=True, context=serializer_context).data

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
        fields = ['id', 'username', 'full_name', 'profile_pic']

    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, instance: UserProfile):
        return f"{instance.first_name} {instance.last_name}"
