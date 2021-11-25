from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('list', views.BoardViewSet)
router.register('collaborator', views.CollaboratorViewSet)
router.register('note', views.NoteViewSet)
router.register('section', views.SectionViewSet)


urlpatterns = router.urls
