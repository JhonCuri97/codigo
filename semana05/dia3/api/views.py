from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import LoginSerializer
# Create your views here.

class IndexView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        context={
            'mensaje':'Bienvenido a mi api'
        }
        return Response(context)

class LoginApiView(APIView):
    
    def post(self,request):
        
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token=serializer.save()
        
        context = {
            "token":token
        }
        return Response(context)