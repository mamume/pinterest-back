from rest_framework.viewsets import ModelViewSet
from .serializers import BoardSerializer, CollaboratorSerializer
from .models import Board, Collaborator


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class CollaboratorViewSet(ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer
