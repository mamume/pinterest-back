from django.urls import path, include
from .views import *




urlpatterns = [
    path('signup', signup, name='user-signup'),
    path('details', profile_details, name='user-details'),
    path('<str:un>/details', profile_details, name='userame-details'),
    path('<int:u_id>/follow', follow, name='follow'),
    path('<int:u_id>/unfollow', unFollow, name='unfollow'),
    path('deactivate', deactivate, name='deactivate'),
    path('activate', activate, name='activate'),
    path('update-password', update_password, name='update-password'),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
]