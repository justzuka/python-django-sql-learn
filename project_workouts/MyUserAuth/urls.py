from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path("login", views.login),
    path("signup", views.signup),
    path("test_token", views.test_token),
]
