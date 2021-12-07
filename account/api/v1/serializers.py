from logging import StreamHandler
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from account.models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class FollowingSerializer(serializers.ModelSerializer):
    followed_user = serializers.StringRelatedField()

    class Meta:
        model = UserFollowing
        fields = ['id', 'followed_user', 'start_follow']


class FollowerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserFollowing
        fields = ['id', 'user', 'start_follow']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'text', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
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
            'website',

        ]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user = UserProfile(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            age=self.validated_data.get('age'),
            bio=self.validated_data.get('bio'),
            gender=self.validated_data.get('gender'),
            country=self.validated_data.get('country'),
            profile_pic=self.validated_data.get('profile_pic'),
            website=self.validated_data.get('website')
        )

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('check old password again')

    def validate_new_password(self, value):
        try:
            validate_password(value, self.context['request'].user)
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value

    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class resetPasswordCompleteSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    uid64 = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    class Meta:
        fields = ['password', 'uid64', 'token']

    def validate_password(self, value):
        try:
            validate_password(value)
        except Exception as e:
            raise serializers.ValidationError(str(e), code=400)
        return value

    def save(self, **kwargs):

        uid64 = self.validated_data['uid64']
        token = self.validated_data['token']
        id = smart_str(urlsafe_base64_decode(uid64))
        user = UserProfile.objects.get(id=id)
        # print(user, token)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise AuthenticationFailed(
                detail='link has been expired', code=401)

        user.set_password(self.validated_data['password'])
        user.save()
        return user


class UserDataSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    follower = serializers.SerializerMethodField()
    notification = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
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
            'website',

        ]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        user = UserProfile(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            age=self.validated_data.get('age'),
            bio=self.validated_data.get('bio'),
            gender=self.validated_data.get('gender'),
            country=self.validated_data.get('country'),
            profile_pic=self.validated_data.get('profile_pic'),
            website=self.validated_data.get('website')
        )

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user

    def get_following(self, obj):
        if obj.following:
            return FollowingSerializer(obj.following.all(), many=True).data

    def get_follower(self, obj):
        if obj.follower:
            return FollowerSerializer(obj.follower.all(), many=True).data

    def get_notification(self, obj):
        if obj.notification:
            return NotificationSerializer(obj.notification.all(), many=True).data
