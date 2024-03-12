from rest_framework import serializers
from .models import Exercise, WorkoutPlan

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'  # Include all fields of the Exercise model

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'  # Include all fields by default