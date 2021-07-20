from rest_framework.views import APIView
from .models import User
from . serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserView(APIView):

    @staticmethod
    def get(request, pk):
        user = User.objects.filter(pk=pk)
        if user is None:
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

