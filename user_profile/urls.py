from django.urls import path
from . import views

url_patterns = [
    path("<int:id>/", views.profile_detail, name="profile-detail")
]
