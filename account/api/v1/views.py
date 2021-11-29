from rest_framework import response
from rest_framework.response import Response
from django.http import request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from account.models import UserFollowing, UserProfile
from .serializers import UpdatePasswordSerializer, UserDataSerializer, UserSerializer
from oauth2_provider.models import AccessToken
from oauth2_provider.models import RefreshToken
from django.utils import timezone



@api_view(['POST'])
@permission_classes([])
def signup(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        obj = AccessToken.objects.get(user__email=request.data['email'])
        tokens={
            'access_token':obj.token,
            'expires_in':36000,
            'token_type':'Bearer',
            'scope':obj.scope,
            'refresh_token':RefreshToken.objects.get(user__email=request.data['email']).token
        }
        return Response(data=tokens, status=status.HTTP_201_CREATED)
    else:
        return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile_details(request, **kwargs):
    if kwargs:
        user = UserProfile.objects.filter(username=kwargs['un'])
    else:
        user = UserProfile.objects.filter(username=request.user)
    if user.exists():
        ser_user = UserDataSerializer(
            instance=user.first(), context={'request': request})
        return Response(data=ser_user.data, status=status.HTTP_200_OK)
    else:
        return Response(data={'msg': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def follow(request, u_id):

    f_user = UserProfile.objects.filter(id=u_id)
    if f_user.exists():
        follow = UserFollowing.objects.create(
            user=request.user, followed_user=f_user.first())
        return Response(data={'msg': follow.__str__()}, status=status.HTTP_201_CREATED)

    else:
        return Response(data={'msg': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def unFollow(request, u_id):
    f_user = UserProfile.objects.filter(id=u_id)

    if f_user.exists():
        try:
            UserFollowing.objects.get(
                user=request.user, followed_user=f_user.first()).delete()

            return Response(data={'msg': f"{request.user} unfollowed {f_user.first().username}"}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={'msg': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def deactivate(request):
    data = {'is_active': False}
    user = UserProfile.objects.get(id=request.user.id)
    ser_user = UserSerializer(instance=user)
    ser_user.update(instance=user, validated_data=data)
    return Response(data=ser_user.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_profile(request):
    ser_user = UserSerializer(instance=request.user, data=request.data)
    if ser_user.is_valid():
        ser_user.update(instance=request.user, validated_data=request.data)
        return Response(data={'msg':'updated successfully'}, status=status.HTTP_200_OK)
    return Response(data=ser_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([])
def activate(request):
    user = UserProfile.objects.filter(email=request.data['email'])
    if user.exists():
        if not user.first().check_password(request.data['password']):
            return Response(data={'msg': 'incorrect passsword'})
        data = {'is_active': True}
        try:
            ser_user = UserSerializer(instance=user.first())
            ser_user.update(instance=user.first(), validated_data=data)
            # token = create_token(user.first())
            return Response(data={'token': 'token'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'msg': e})
    else:
        return Response(data={'msg': 'user not found'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def update_password(request):
    serializer = UpdatePasswordSerializer(
        data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(data={'msg': 'password changed successfuly'}, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request):
    try:
        UserProfile.objects.get(username=request.user).delete()
        return Response(data={'msg':'account deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'msg':f"error while delete {e}"})
