from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token



urlpatterns = [
    path('signup', signup, name='user-signup'),
    # path('login', obtain_auth_token, name='user-login'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/auth', obtain_jwt_token, name='auth-token'),
    path('api/token/refresh/jwt', refresh_jwt_token, name='refresh-token'),
    path('details', profile_details, name='user-details'),
    path('<str:un>/details', profile_details, name='userame-details'),
    path('<int:u_id>/follow', follow, name='follow'),
    path('<int:u_id>/unfollow', unFollow, name='unfollow'),
    path('deactivate', deactivate, name='deactivate'),
    path('activate', activate, name='activate'),
    path('update-password', update_password, name='update-password')
    
]