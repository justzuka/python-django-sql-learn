from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exercise, Goal, WorkoutPlan, WorkoutPlanExercise  # Import the Exercise model
from .serializers import ExerciseSerializer, GoalSerializer, WorkoutPlanExerciseSerializer, WorkoutPlanSerializer  # Import the ExerciseSerializer

from rest_framework import status   

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def default_exercises(request):
    exercises = Exercise.objects.all().order_by('name')  # Order by name for better presentation
    serializer = ExerciseSerializer(exercises, many=True)  # Serialize all exercises
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_default_exercises_with_ids(request):
    # Get the exercise IDs from the request
    exercise_ids = request.data.get("exercises")

    # Filter the exercises based on the IDs
    exercises = Exercise.objects.filter(id__in=exercise_ids)

    # Serialize the filtered exercises
    serializer = ExerciseSerializer(exercises, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_workout_plan(request):
    serializer = WorkoutPlanSerializer(data={**request.data, 'user': request.user.id})
    
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_workout_plans(request):
    workout_plans = WorkoutPlan.objects.filter(user=request.user.id).order_by('-id')
    
    serializer = WorkoutPlanSerializer(workout_plans, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_workout_plan_exercise(request):

    workout_plan_id = request.data.get('workout_plan')
    
    # if the workout plan does not exist or does not belong to the user
    if not WorkoutPlan.objects.filter(id=workout_plan_id, user=request.user).exists():
        return Response({'error': 'WorkoutPlan not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WorkoutPlanExerciseSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_workout_plan_exercises(request):
    workout_plan_id = request.data.get('workout_plan')

    # Check if the WorkoutPlan with the given ID belongs to the authenticated user
    if not WorkoutPlan.objects.filter(id=workout_plan_id, user=request.user).exists():
        return Response({'error': 'WorkoutPlan not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)
    
    # Retrieve all WorkoutPlanExercise instances for the given WorkoutPlan
    workout_plan_exercises = WorkoutPlanExercise.objects.filter(workout_plan_id=workout_plan_id)
    serializer = WorkoutPlanExerciseSerializer(workout_plan_exercises, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_frequency_choices(request):
    # Get the choices from the WorkoutPlan model
    choices = WorkoutPlan._meta.get_field('frequency').choices

    # Convert the choices to a dictionary
    choices_dict = {key: value for key, value in choices}

    # Return the choices as a JSON response
    return Response(choices_dict, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_goal_type_choices(request):
    # Get the choices from the Goal model
    choices = Goal._meta.get_field('type').choices

    # Convert the choices to a dictionary
    choices_dict = {key: value for key, value in choices}

    # Return the choices as a JSON response
    return Response(choices_dict, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_goal(request):
    data = request.data.copy()
    data['user'] = request.user.id

    # Create a serializer with the request data
    serializer = GoalSerializer(data=data)

    # If the serializer is valid, save the goal and return it
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_goal(request):
    goal_id = request.data.get('id')
    try:
        goal = Goal.objects.get(id=goal_id, user=request.user)
    except Goal.DoesNotExist:
        return Response({'error': 'Goal not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)

    # Create a serializer with the request data
    serializer = GoalSerializer(goal, data=request.data, partial=True)

    # If the serializer is valid, save the goal and return it
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_goal(request):
    goal_id = request.data.get('id')
    try:
        # Get the goal that belongs to the authenticated user and has the given ID
        goal = Goal.objects.get(id=goal_id, user=request.user)
    except Goal.DoesNotExist:
        return Response({'error': 'Goal not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the goal
    serializer = GoalSerializer(goal)

    # Return the serialized goal
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_goals(request):
    # Get all goals that belong to the authenticated user
    goals = Goal.objects.filter(user=request.user)

    # Serialize the goals
    serializer = GoalSerializer(goals, many=True)

    # Return the serialized goals
    return Response(serializer.data, status=status.HTTP_200_OK)