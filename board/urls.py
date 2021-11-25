from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.BoardDetail.as_view(), name="board-detail")
]
