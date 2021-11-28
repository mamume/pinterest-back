from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from account.models import UserProfile
from rest_framework.decorators import api_view, permission_classes

@permission_classes([])
class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        username = self.request.query_params.get('username')

        if username:
            queryset = queryset.filter(username=username)

        return queryset
