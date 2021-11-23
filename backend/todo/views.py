from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()