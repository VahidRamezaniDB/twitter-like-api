from django.urls import path
from .views import UserView


urlpatterns = [
    path('create/', UserView.as_view()),
    path('<int:pk>/', UserView.as_view())
]