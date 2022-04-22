from django.urls import path 
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('users/currentUser/<int:pk>/', CurrentUserView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('profiles/', ProfileListView.as_view())
]