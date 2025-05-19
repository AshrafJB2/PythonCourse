from django.urls import path
from .views import ListMenu, RetrieveUpdateDestroyMenu, CreateUser, CreateMenu
from .views import CustomLoginView

urlpatterns = [
    path('resto/', ListMenu.as_view(), name='list'),
    path('resto/create/', CreateMenu.as_view(), name='create'),
    path('resto/<int:pk>/', RetrieveUpdateDestroyMenu.as_view(), name='retreiveupdatedestroy'),
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    
    
]
