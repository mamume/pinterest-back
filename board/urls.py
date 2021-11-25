from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('list', views.BoardViewSet)
router.register('collaborator', views.CollaboratorViewSet)


urlpatterns = router.urls
