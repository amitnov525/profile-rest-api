from django.shortcuts import render

from rest_framework.views import  APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """TEST API VIEW"""
    def get(self,request,format=None):
        """Returns a list of API features"""

        api_view=[
            'This is a demonstration of API View',
        ]
        return Response({'message':'This is an view','api_view':api_view})
    
