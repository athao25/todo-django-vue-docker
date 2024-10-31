from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import TodoItemSerializer
from .models import TodoItem

# Create your views here.
class TodoItemListCreate(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    def delete(self, request, *args, **kwargs):
        TodoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TodoItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'pk'