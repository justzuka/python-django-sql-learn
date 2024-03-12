from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exercise, WorkoutPlan  # Import the Exercise model
from .serializers import ExerciseSerializer, WorkoutPlanSerializer  # Import the ExerciseSerializer

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