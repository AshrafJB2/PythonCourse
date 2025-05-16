from django.urls import path
from .views import ListCreateMenu, RetrieveUpdateDestroyMenu
urlpatterns = [
    path('resto/', ListCreateMenu.as_view(), name='listcreate'),
    path('resto/<int:pk>/', RetrieveUpdateDestroyMenu.as_view(), name='retreiveupdatedestroy'),
]
