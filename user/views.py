from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User
from post.models import Post
from post.serializer import PostSerializer
from . serializer import UserSerializer, UserLogInSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def login_views(req):
    user_obj = UserLogInSerializer(data=req.data)
    if not user_obj.is_valid():
        return Response({"error": "Not valid args!"}, status=status.HTTP_400_BAD_REQUEST)
    username = user_obj["username"].value
    user = User.objects.filter(userName=username)
    if len(user) != 0:
        user = user[0]
        if user.password == user_obj["password"].value:
            posts = Post.objects.filter(user=user.id)
            if len(posts) == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)
            ser_posts = PostSerializer(posts, many=True)
            return Response(ser_posts.data, status=status.HTTP_200_OK)
    return Response({"error": "username or password is incorrect"}, status=status.HTTP_403_FORBIDDEN)


class UserView(APIView):

    @staticmethod
    def get(request, pk):
        user = User.objects.filter(pk=pk)
        if len(user) == 0:
            return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        user = user[0]
        user_ser = UserSerializer(user)
        return Response(user_ser.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "not valid arguments"}, status=status.HTTP_400_BAD_REQUEST)

