from django.urls import path, include
from . import views

urlpatterns = [
    path('default-exercises', views.default_exercises),
]
