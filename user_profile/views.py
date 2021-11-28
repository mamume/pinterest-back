from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from .serializers import ProfileSerializer
from account.models import UserProfile


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        username = self.request.query_params.get('username')

        if username:
            queryset = queryset.filter(username=username)
        else:
            queryset = queryset.filter(username=self.request.user)

        return queryset
