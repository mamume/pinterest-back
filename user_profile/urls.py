from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('list', views.ProfileViewSet, basename='profile-list')
router.register('details', views.ProfileDetailsViewSet,
                basename='profile-details')
router.register('update', views.ProfileUpdateViewSet,
                basename='profile-update')
router.register('followers', views.FollowersViewSet, basename='followers-list')
router.register('following', views.FollowingViewSet, basename='following-list')
router.register('pins-delete', views.PinDeleteViewSet, basename='pins-delete')

urlpatterns = router.urls
