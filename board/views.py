from rest_framework.viewsets import ModelViewSet

from .serializers import BoardSerializer, CollaboratorSerializer, NoteSerializer, SectionSerializer
from .models import Board, Collaborator, Note, Section


class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer

    def get_queryset(self):
        queryset = Board.objects.all()
        owner_id = self.request.query_params.get('owner_id')
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)

        return queryset


class CollaboratorViewSet(ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        board_id = self.request.query_params.get('board_id')
        if board_id:
            queryset = queryset.filter(board_id=board_id)

        return queryset


class SectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = Section.objects.all()
        board_id = self.request.query_params.get('board_id')
        if board_id:
            queryset = queryset.filter(board_id=board_id)

        return queryset
