from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exercise, Goal, WorkoutPlan, WorkoutPlanExercise  # Import the Exercise model
from .serializers import ExerciseSerializer, GoalSerializer, WorkoutPlanExerciseSerializer, WorkoutPlanSerializer  # Import the ExerciseSerializer

from rest_framework import status   

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get a list of all default exercises.',
    security=[{'Bearer': []}],
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def default_exercises(request):
    exercises = Exercise.objects.all().order_by('name')  # Order by name for better presentation
    serializer = ExerciseSerializer(exercises, many=True)  # Serialize all exercises
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get a list of default exercises by their IDs.',
    manual_parameters=[
        openapi.Parameter(
            'exercises', 
            openapi.IN_QUERY, 
            description='The IDs of the exercises', 
            type=openapi.TYPE_ARRAY, 
            items=openapi.Items(type=openapi.TYPE_INTEGER)
        ),
    ],
    security=[{'Bearer': []}],
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_default_exercises_with_ids(request):
    # Get the exercise IDs from the request
    exercise_ids_string = request.GET.get("exercises", "")
    exercise_ids = exercise_ids_string.split(",")
    exercise_ids = [int(id) for id in exercise_ids]

    # Filter the exercises based on the IDs
    exercises = Exercise.objects.filter(id__in=exercise_ids)

    # Serialize the filtered exercises
    serializer = ExerciseSerializer(exercises, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='post',
    operation_description='This endpoint allows authenticated users to create a new workout plan.',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='The name of the workout plan'),
            'frequency': openapi.Schema(type=openapi.TYPE_INTEGER, description='The frequency of the workout plan'),
            'goal': openapi.Schema(type=openapi.TYPE_STRING, description='The goal of the workout plan'),
            'duration': openapi.Schema(type=openapi.TYPE_INTEGER, description='The duration of the workout plan'),
        },
        required=['name', 'frequency', 'goal', 'duration'],
    ),
    security=[{'Bearer': []}],
)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_workout_plan(request):
    serializer = WorkoutPlanSerializer(data={**request.data, 'user': request.user.id})
    
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get a list of all their workout plans.',
    security=[{'Bearer': []}],
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_workout_plans(request):
    workout_plans = WorkoutPlan.objects.filter(user=request.user.id).order_by('-id')
    
    serializer = WorkoutPlanSerializer(workout_plans, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='post',
    operation_description='This endpoint allows authenticated users to add an exercise to a workout plan.',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'workout_plan': openapi.Schema(type=openapi.TYPE_INTEGER, description='The ID of the workout plan'),
            'exercise': openapi.Schema(type=openapi.TYPE_INTEGER, description='The ID of the exercise'),
            'repetitions': openapi.Schema(type=openapi.TYPE_INTEGER, description='The number of repetitions for the exercise'),
            'sets': openapi.Schema(type=openapi.TYPE_INTEGER, description='The number of sets for the exercise'),
            'duration': openapi.Schema(type=openapi.TYPE_INTEGER, description='The duration of the exercise in minutes'),
            'distance': openapi.Schema(type=openapi.TYPE_INTEGER, description='The distance for the exercise in meters'),
        },
        required=['workout_plan', 'exercise', 'repetitions', 'sets', 'duration', 'distance'],
    ),
    security=[{'Bearer': []}],
)
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


@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get exercises for a specific workout plan by its ID.',
    manual_parameters=[
        openapi.Parameter(
            'workout_plan_id', 
            openapi.IN_PATH, 
            description='The ID of the workout plan', 
            type=openapi.TYPE_INTEGER
        ),
    ],
    security=[{'Bearer': []}],
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_workout_plan_exercises(request, workout_plan_id):
    # Check if the WorkoutPlan with the given ID belongs to the authenticated user
    if not WorkoutPlan.objects.filter(id=workout_plan_id, user=request.user).exists():
        return Response({'error': 'WorkoutPlan not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)
    
    # Retrieve all WorkoutPlanExercise instances for the given WorkoutPlan
    workout_plan_exercises = WorkoutPlanExercise.objects.filter(workout_plan_id=workout_plan_id)
    serializer = WorkoutPlanExerciseSerializer(workout_plan_exercises, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get the frequency choices for a WorkoutPlan.',
    security=[{'Bearer': []}],
)
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

@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get the goal type choices.',
    security=[{'Bearer': []}],
)
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

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'type': openapi.Schema(type=openapi.TYPE_STRING, description='The type of the goal'),
        'weight_target': openapi.Schema(type=openapi.TYPE_NUMBER, description='The target weight for weight loss/gain goals'),
        'exercise': openapi.Schema(type=openapi.TYPE_INTEGER, description='The exercise for exercise-specific goals'),
        'target_value': openapi.Schema(type=openapi.TYPE_INTEGER, description='The target value for the exercise'),
    },
    required=['type'],
),security=[{'Bearer': []}],)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_goal(request):
    """
    Create a new goal for the authenticated user.

    Parameters:
    - request: The HTTP request. The request data should contain the fields for the goal.

    Returns:
    - The created goal as a JSON object, or an error message if the request data is not valid.
    """
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
    

@swagger_auto_schema(
    method='put',
    operation_description='This endpoint allows authenticated users to update a specific goal by its ID.',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='The ID of the goal'),
            'type': openapi.Schema(type=openapi.TYPE_STRING, description='The type of the goal'),
            'weight_target': openapi.Schema(type=openapi.TYPE_NUMBER, description='The weight target of the goal'),
            'exercise': openapi.Schema(type=openapi.TYPE_INTEGER, description='The exercise of the goal'),
            'target_value': openapi.Schema(type=openapi.TYPE_INTEGER, description='The target value of the goal'),
        },
    ),
    security=[{'Bearer': []}],
)
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
    
@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get a specific goal by its ID.',
    manual_parameters=[
        openapi.Parameter(
            'goal_id', 
            openapi.IN_PATH, 
            description='The ID of the goal', 
            type=openapi.TYPE_INTEGER
        ),
    ],
    security=[{'Bearer': []}],
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_goal(request, goal_id):
    try:
        # Get the goal that belongs to the authenticated user and has the given ID
        goal = Goal.objects.get(id=goal_id, user=request.user)
    except Goal.DoesNotExist:
        return Response({'error': 'Goal not found or does not belong to the user'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the goal
    serializer = GoalSerializer(goal)

    # Return the serialized goal
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    operation_description='This endpoint allows authenticated users to get a list of all their goals.',
    security=[{'Bearer': []}],
)
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