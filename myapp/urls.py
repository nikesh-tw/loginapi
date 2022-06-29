from django.urls import path
from .views import RegisterApi


urlpatterns = [
    path('',RegisterApi.as_view()),
    path('register/', RegisterApi.as_view(), name='register'),
]