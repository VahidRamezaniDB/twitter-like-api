from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .models import Comment


class CommentView(APIView):

    def get(self, req, pk):
        comment = Comment.objects.filter(pk=pk)
        if len(comment) == 0:
            return Response({"error": "Not found!"}, status=status.HTTP_404_NOT_FOUND)
        comment = comment[0]
        ser_comment = CommentSerializer(comment)
        return Response(ser_comment.data, status=status.HTTP_200_OK)

    def delete(self, req, pk):
        comment = Comment.objects.filter(pk=pk)
        if len(comment) == 0:
            return Response({"error": "Not found!"}, status=status.HTTP_404_NOT_FOUND)
        comment = comment[0]
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, req, pk):
        comment = Comment.objects.filter(pk=pk)
        if len(comment) == 0:
            return Response({"error": "Not found!"}, status=status.HTTP_404_NOT_FOUND)
        comment = comment[0]
        comment.like()
        comment.save()
        ser_comment = CommentSerializer(comment)
        return Response(ser_comment.data, status=status.HTTP_200_OK)

    def post(self, req):
        comment = CommentSerializer(data=req.data)
        if not comment.is_valid():
            return Response({"error": "Not valid args"}, status=status.HTTP_400_BAD_REQUEST)
        comment.save()
        return Response(comment.data, status=status.HTTP_200_OK)
