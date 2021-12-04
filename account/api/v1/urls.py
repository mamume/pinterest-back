from django.urls import path, include
from .views import *




urlpatterns = [
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('signup', signup, name='user-signup'),
    path('details', profile_details, name='user-details'),
    path('<str:un>/details', profile_details, name='userame-details'),
    path('<int:u_id>/follow', follow, name='follow'),
    path('<int:u_id>/unfollow', unFollow, name='unfollow'),
    path('deactivate', deactivate, name='deactivate'),
    path('activate', activate, name='activate'),
    path('update-password', update_password, name='update-password'),
    path('update', update_profile, name='update-profile'),
    path('delete', delete_user, name='delete-user'),
    path('password-reset-request', resetPasswordRequest, name='password-reset-request'),
    path('password-reset-check/<str:uid64>/<str:token>', resetPasswordCheck, name='password-reset-check'),
    path('password-reset-complete', resetPasswordComplete, name='password-reset-complete'),
    path('checkmail', checkmail, name='checkmail'),
    path('checkuser', checkuser, name='checkuser')

]