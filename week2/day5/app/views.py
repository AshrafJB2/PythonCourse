from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer
from .models import MenuItems


class ListCreateMenu(ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer


class RetrieveUpdateDestroyMenu(RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer