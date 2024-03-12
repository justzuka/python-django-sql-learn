from django.urls import path, include
from . import views

urlpatterns = [
    path('default-exercises', views.default_exercises),
    path('create-workout-plan', views.create_workout_plan),
    path('get-all-workout-plans', views.get_all_workout_plans),
]
