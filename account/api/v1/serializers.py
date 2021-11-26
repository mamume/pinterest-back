from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.models import *

User = get_user_model()

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['id', 'following_user_id', 'start_follow']

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['id', 'user_id', 'start_follow']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'text', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    follower = serializers.SerializerMethodField()
    notification = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'age', 
            'gender', 
            'country', 
            'bio', 
            'profile_pic',
            'following',
            'follower',
            'notification',
        ]
        extra_kwargs = {'password':{'write_only':True}}
    
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_follower(self, obj):
        return FollowerSerializer(obj.follower.all(), many=True).data

    def get_notification(self, obj):
        return NotificationSerializer(obj.notification.all(), many=True).data

    def save(self, **kwargs):
        user = User(
            email = self.validated_data.get('email'),
            username = self.validated_data.get('username'),
            first_name = self.validated_data.get('first_name'),
            last_name = self.validated_data.get('last_name'),
            age = self.validated_data.get('age'),
            bio = self.validated_data.get('bio'),
            gender = self.validated_data.get('gender'),
            country = self.validated_data.get('country'),
            profile_pic = self.validated_data.get('profile_pic'),
                
            )

        user.set_password(self.validated_data.get('password'))
        user.save()

        return user
