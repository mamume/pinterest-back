from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from account.models import UserFollowing, UserProfile
from .serializers import *
from oauth2_provider.models import AccessToken
from oauth2_provider.models import RefreshToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from account.utils import Util


@api_view(['POST'])
@permission_classes([])
def signup(request):
    # print(request.data)
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        try:
            obj = AccessToken.objects.get(user__email=request.data['email'])
            tokens = {
                'access_token': obj.token,
                'expires_in': 36000,
                'token_type': 'Bearer',
                'scope': obj.scope,
                'refresh_token': RefreshToken.objects.get(user__email=request.data['email']).token
            }
        except:
            tokens = {
                'access_token': "",
                'expires_in': "",
                'token_type': '',
                'scope': "",
                'refresh_token': ""
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
    ser_user = UserSerializer(instance=request.user,
                              data=request.data, partial=True)
    if ser_user.is_valid():
        ser_user.update(instance=request.user, validated_data=request.data)
        return Response(data={'msg': 'updated successfully'}, status=status.HTTP_200_OK)
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
        return Response(data={'msg': 'account deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'msg': f"error while delete {e}"})


@api_view(['POST'])
@permission_classes([])
def resetPasswordRequest(request):
    email = request.data['email']
    if UserProfile.objects.filter(email=email).exists():
        # print('good')
        user = UserProfile.objects.get(email=email)
        uid64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        redirect_url = request.data['redirect_url']
        current_site = 'localhost:8000'
        relative_site = reverse(
            'password-reset-check',
            kwargs={'uid64': uid64, 'token': token}
        )
        absurl = f"http://{current_site}{relative_site}"
        email_body = f"you requested an email to reset your password \n please use the link below \n {absurl}?redirect_url={redirect_url}"
        data = {
            'email_body': email_body,
            'email_subject': 'reset password request',
            'to_email': [user.email]
        }
        Util.send_email(data)
        return Response({'success': 'we sent an email to reset your password'}, status=status.HTTP_200_OK)
    return Response({'error': f"{email} isn't in our database"})


@api_view(['GET'])
@permission_classes([])
def resetPasswordCheck(request, uid64, token):
    redirect_url = request.GET.get('redirect_url')
    try:
        id = smart_str(urlsafe_base64_decode(uid64))
        user = UserProfile.objects.get(id=id)
        # print(user)

        if not PasswordResetTokenGenerator().check_token(user, token):
            return redirect(f"{redirect_url}?token_valid=false")

        return redirect(f"{redirect_url}?token_valid=true&uid64={uid64}&token={token}")

    except DjangoUnicodeDecodeError as error:
        return redirect(f"{redirect_url}?token_valid=false")


@api_view(['PATCH'])
@permission_classes([])
def resetPasswordComplete(request):
    serializer = resetPasswordCompleteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={'success': 'Password reseted successfully'}, status=status.HTTP_200_OK)

    return Response(data=serializer.errors)


@api_view(['POST'])
@permission_classes([])
def checkmail(request):
    user = UserProfile.objects.filter(email=request.data['email'])
    if user.exists():
        return Response(data={"fail": True}, status=status.HTTP_200_OK)
    else:
        return Response(data={'success': True}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([])
def checkuser(request):
    user = UserProfile.objects.filter(username=request.data['username'])
    if user.exists():
        return Response(data={"fail": False}, status=status.HTTP_200_OK)
    else:
        return Response(data={'success': True}, status=status.HTTP_200_OK)
