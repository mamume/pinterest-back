from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('list', views.BoardViewSet, basename='board-list')
router.register('update', views.BoardUpdateViewSet, basename='board-update')
router.register('collaborator', views.CollaboratorViewSet,
                basename='collaborator-list')
router.register('note', views.NoteViewSet, basename='note-list')
router.register('section', views.SectionViewSet, basename='section-list')

urlpatterns = router.urls
