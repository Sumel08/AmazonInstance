from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    '''Test API View.'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features.'''

        an_apiView = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over you logic',
            'Is mapped manually to URL\'s'
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        '''Create a Hello message with our name'''

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handles updating an object'''

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        '''Handles partially update of an object'''

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        '''Handles delete object'''

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a new Hello message.'''

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''Handles getting an object by its ID.'''

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''Handles updating an object'''

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        '''Handles updating part of an object'''

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        '''Handles removing an object'''

        return Response({'http_method': 'DELETE'})
