# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#   pass

# class Exercise(models.Model):
#   name = models.CharField(max_length=255)
#   description = models.TextField()
#   instructions = models.TextField()
#   target_muscle_groups = models.CharField(max_length=255)
#   # Add other relevant fields (e.g., image)

# class WorkoutPlan(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   name = models.CharField(max_length=255)
#   frequency = models.IntegerField(choices=(
#       (1, "Daily"),
#       (2, "Every Other Day"),
#       (3, "Twice a Week"),
#       (4, "Three Times a Week"),
#       (5, "Four Times a Week"),
#       (6, "Five Times a Week"),
#       (7, "Six Times a Week"),
#   ))
#   goal = models.CharField(max_length=255)
#   duration = models.IntegerField()

# class WorkoutPlanExercise(models.Model):
#   workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
#   exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#   repetitions = models.IntegerField(null=True, blank=True)  # Optional customization
#   sets = models.IntegerField(null=True, blank=True)  # Optional customization
#   duration = models.IntegerField(null=True, blank=True)  # Optional customization (time)
#   distance = models.FloatField(null=True, blank=True)  # Optional customization (distance)

# class Goal(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   type = models.CharField(max_length=255, choices=(("weight", "Weight Loss/Gain"), ("exercise", "Exercise Specific")))
#   # Weight Goal specific fields
#   weight_target = models.FloatField(null=True, blank=True)
#   # Exercise Specific Goal fields
#   exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
#   target_value = models.IntegerField(null=True, blank=True)  # Reps, sets, duration, etc. depending on exercise

# # Bonus Feature Models (if implemented)
# class WorkoutSession(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
#   date = models.DateField()