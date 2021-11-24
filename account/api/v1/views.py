from rest_framework.response import Response
from django.http import request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()

@api_view(['POST'])
def signup(request): 
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(data={'token':Token.objects.get(user__email=user.data.get('email')).key}, status=status.HTTP_201_CREATED)
    else:
        return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)