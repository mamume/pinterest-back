from rest_framework.viewsets import ModelViewSet
from .serializers import BoardSerializer, CollaboratorSerializer, NoteSerializer, SectionSerializer
from .models import Board, Collaborator, Note, Section


class BoardViewSet(ModelViewSet):
    # queryset = Board.objects.all()
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
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
