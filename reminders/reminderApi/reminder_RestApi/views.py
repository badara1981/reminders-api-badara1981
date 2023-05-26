from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reminder_RestApi.models import Reminder_RestApi
from reminder_RestApi.serializers import Reminder_RestApiSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from reminder_RestApi.serializers import UserSerializer
from django.contrib.auth.models import User


class Reminder_RestApiList(generics.ListCreateAPIView):
    queryset = Reminder_RestApi.objects.all()
    serializer_class = Reminder_RestApiSerializer
    
@api_view(['GET', 'PUT', 'DELETE'])
def reminder_RestApi_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        reminder_RestApi = Reminder_RestApi.objects.get(pk=pk)
    except Reminder_RestApi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Reminder_RestApiSerializer(reminder_RestApi)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Reminder_RestApiSerializer(reminder_RestApi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reminder_RestApi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 

class Reminder_RestApiList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        reminder_RestApi = Reminder_RestApi.objects.all()
        serializer = Reminder_RestApiSerializer(reminder_RestApi, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Reminder_RestApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Reminder_RestApiDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Reminder_RestApi.objects.get(pk=pk)
        except Reminder_RestApi.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reminder_RestApi = self.get_object(pk)
        serializer = Reminder_RestApiSerializer(reminder_RestApi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reminder_RestApi = self.get_object(pk)
        serializer = Reminder_RestApiSerializer(reminder_RestApi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reminder_RestApi = self.get_object(pk)
        reminder_RestApi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Reminder_RestApiList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Reminder_RestApi.objects.all()
    serializer_class = Reminder_RestApiSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    class Reminder_RestApiList(generics.ListCreateAPIView):
        queryset = Reminder_RestApi.objects.all()
        serializer_class = Reminder_RestApiSerializer
    
    class Reminder_RestApiDetails(generics.RetrieveUpdateAPIView):
        queryset = Reminder_RestApi.objects.all()

        serializer_class = Reminder_RestApiSerializer


    class UserList(generics.ListAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer


    class UserDetail(generics.RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

