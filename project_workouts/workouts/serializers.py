from rest_framework import serializers
from .models import Exercise, Goal, WorkoutPlan, WorkoutPlanExercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'  # Include all fields of the Exercise model

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'  # Include all fields by default

class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanExercise
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'