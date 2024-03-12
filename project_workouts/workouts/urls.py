from django.urls import path, include
from . import views

urlpatterns = [
    path('default-exercises', views.default_exercises),
    path('create-workout-plan', views.create_workout_plan),
    path('get-all-workout-plans', views.get_all_workout_plans),
    path('create-workout-plan-exercise', views.create_workout_plan_exercise),
    path('get-workout-plan-exercises', views.get_all_workout_plan_exercises),
]
