from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
# Create your views here.


class TaskList(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes =[]

