from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import UserProfile
from .serializers import ProfileSerializer


@api_view(['GET'])
def profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    serializer = ProfileSerializer(profile)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data)
