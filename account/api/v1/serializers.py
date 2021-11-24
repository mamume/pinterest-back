from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.models import *

User = get_user_model()

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['id', 'following', 'start_follow']

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ['id', 'follower', 'start_follow']

class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    follower = serializers.SerializerMethodField()

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
            'follower'
        ]
        extra_kwargs = {'password':{'write_only':True}}
    
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_follower(self, obj):
        return FollowerSerializer(obj.follower.all(), many=True).data

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
