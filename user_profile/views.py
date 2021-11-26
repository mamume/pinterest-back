from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from account.models import UserProfile


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
