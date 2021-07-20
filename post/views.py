from rest_framework.views import APIView
from .models import Post
from . serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status


class PostViews(APIView):

    @staticmethod
    def get(req, pk):
        post = Post.objects.filter(pk=pk)
        if len(post) == 0:
            return Response({"error": "NotFound!"}, status=status.HTTP_404_NOT_FOUND)
        post = post[0]
        ser_post = PostSerializer(post)
        return Response(ser_post.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(req, pk):
        post = Post.objects.filter(pk=pk)
        if len(post) == 0:
            return Response({"error": "NotFound!"}, status=status.HTTP_404_NOT_FOUND)
        post = post[0]
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def post(req):
        post = PostSerializer(data=req.data)
        if not post.is_valid():
            return Response({"error": "Not valid arguments."}, status=status.HTTP_400_BAD_REQUEST)
        post.save()
        return Response(post.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def put(req, pk):
        post = Post.objects.filter(pk=pk)
        if len(post) == 0:
            return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        post = post[0]
        post.like()
        post.save()
        ser_post = PostSerializer(post)
        return Response(ser_post.data, status=status.HTTP_200_OK)
