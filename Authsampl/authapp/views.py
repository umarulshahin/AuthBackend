from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializer import NoteSerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenobtainedPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    

@api_view(['GET'])
def getRouter(request):
    
    router=[
        '/api/token',
        '/api/token/refresh',
    ]
   
    return Response(router)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getNote(request):
    
    user=request.user
    Notes=user.note_set.all()
    serializer=NoteSerializer(Notes,many=True)
    
    return Response(serializer.data)
    