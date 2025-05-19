from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import MenuSerializer, UserSerializer
from .models import MenuItems
from .permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from app.models import TheUser

class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        try:
            user = TheUser.objects.get(username=username)
            if user.password == password:
                return Response({"token": TheUser.objects.get(username=username).role})
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
        except TheUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)



class ListMenu(ListAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer

class CreateMenu(CreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdmin]


class RetrieveUpdateDestroyMenu(RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdmin]

class CreateUser(CreateAPIView):
    serializer_class = UserSerializer