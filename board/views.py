from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BoardSerializer
from .models import Board


class BoardDetail(APIView):
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardSerializer(board, context={'request': request})

        return Response(serializer.data)
