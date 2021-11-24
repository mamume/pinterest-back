from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from account.models import UserProfile


@api_view(['GET'])
def profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)

    return Response()
