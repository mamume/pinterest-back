from rest_framework import request
from rest_framework.viewsets import ModelViewSet

from pin.models import Pin
from .serializers import PinDeleteSerializer, ProfileSerializer
from account.models import UserProfile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from .serializers import ProfileSerializer, UserFolloweingSerializer, UserFollowersSerializer
from account.models import UserFollowing, UserProfile


@permission_classes([])
class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')

        if username:
            return UserProfile.objects.filter(username=username)

        return UserProfile.objects.filter(username=self.request.user)


class FollowersViewSet(ModelViewSet):
    serializer_class = UserFollowersSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            follower = UserProfile.objects.get(username=username)
            return UserFollowing.objects.filter(followed_user=follower)

        return UserFollowing.objects.filter(followed_user=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}


class FollowingViewSet(ModelViewSet):
    serializer_class = UserFolloweingSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            following = UserProfile.objects.get(username=username)
            return UserFollowing.objects.filter(user=following)

        return UserFollowing.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}


class PinDeleteViewSet(ModelViewSet):
    serializer_class = PinDeleteSerializer
    queryset = Pin.objects.all()
