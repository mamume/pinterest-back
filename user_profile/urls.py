from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('list', views.ProfileViewSet, basename='profile-list')
router.register('followers', views.FollowersViewSet, basename='followers-list')
router.register('following', views.FollowingViewSet, basename='following-list')

urlpatterns = router.urls
