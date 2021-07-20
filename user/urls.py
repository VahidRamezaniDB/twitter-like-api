from django.urls import path
from .views import UserView


urlpatterns = [
    path('create/', UserView.as_view()),
    path('details/<int:pk>/', UserView.as_view()),
    path('delete/<int:pk>', UserView.as_view()),
]
