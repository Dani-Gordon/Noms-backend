from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/', ListView.as_view()),
    path('recipes/create/', CreateView.as_view()),
    path('recipes/detail/<int:pk>/', DetailView.as_view()),
    path('recipes/<int:pk>/like/', LikeView.as_view()),
    path('recipes/liked/', LikedListView.as_view()),
]
    