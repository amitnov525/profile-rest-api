from django.shortcuts import render

from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app.serializers import Helloserializer


class HelloAPIView(APIView):
    """TEST API VIEW"""
    serializer_class=Helloserializer
    def get(self,request,format=None):
        """Returns a list of API features"""

        api_view=[
            'This is a demonstration of API View',
        ]
        return Response({'message':'This is an view','api_view':api_view})
    
    def post(self,request):
        """Craete a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        """Update user deatils"""
        return Response({'method':'Put'})

    def patch(self,request,pk=None):
        """Partial Update"""
        return Response({'method':'Patch'})
    def delete(self,request,pk=None):
        """Destroy  Object"""
        return Response({'method':'Delete'})
    
    


    
