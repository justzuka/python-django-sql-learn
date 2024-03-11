from django.contrib.auth.models import User
from django.db import models

# exercises
class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    target_muscle_groups = models.CharField(max_length=255)

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    frequency = models.IntegerField(choices=((1, "Daily"), (2, "Every Other Day"), (3, "Once in a week")))
    goal = models.CharField(max_length=255)
    duration = models.IntegerField()

class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField(null=True, blank=True)
    sets = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=(("weight", "Weight Loss/Gain"), ("exercise", "Exercise Specific")))
    weight_target = models.FloatField(null=True, blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    target_value = models.IntegerField(null=True, blank=True)  # Reps, sets, duration, etc. depending on exercise
