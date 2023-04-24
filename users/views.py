from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from users.models import User
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer, UserProflieSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
# Create your views here.


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "good"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomToekonObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user.is_admin = True
        user.save()
        return Response('get요청')


class ProfileView(APIView):

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProflieSerializer(user)

        return Response(serializer.data)


class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("unfollow", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("follow", status=status.HTTP_200_OK)
