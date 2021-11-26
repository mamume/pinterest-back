from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('list', views.ProfileViewSet, basename='profile-list')

urlpatterns = router.urls
