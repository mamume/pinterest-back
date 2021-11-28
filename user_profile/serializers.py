from rest_framework import serializers
from account.models import UserProfile, UserFollowing


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
