from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BoardSerializer


class BoardDetail(APIView):
    def get(self, request, pk):
        board = get_object_or_404(pk=pk)
        serializer = BoardSerializer(board)

        return Response(serializer.data)
