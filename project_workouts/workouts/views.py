from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Exercise  # Import the Exercise model
from .serializers import ExerciseSerializer  # Import the ExerciseSerializer

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
    return Response(serializer.data)
