from django.shortcuts import render
from profiles_app import serializers

from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app.serializers import Helloserializer
from rest_framework import viewsets


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
    

class HelooViewset(viewsets.ViewSet):
    """Viewset Demonstration"""
    serializer_class=Helloserializer

    def list(self,request):
        """Returns a Hello Message"""
        api_list=['Thsi is a simple viewset']
        return Response({'message':'Hello','api_list':api_list})
    
    def create(self,request):
        """It creates an object"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello{name}'
            return Response({'message':message})
    def update(self,request,pk=None):
        """It updates an object """
        return Response({'method':'update'})
    
    def partial_update(self,request,pk=None):
        """It partial update an item"""
        return Response({'method':'partial_update'})
    
    def retrieve(self,request,pk=None):
        """It retrieve an object"""
        return Response({'method':'retrieve'})
    
    def destroy(self,request,pk=None):
        """It delete an object"""
        return Response({'method':'destroy'})
    




    
    


    
