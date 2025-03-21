from django.shortcuts import render
from .serializers import UserSerializer,AssigneesSerializer
from .models import Assignees
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class AssigneeViewSet(viewsets.ModelViewSet):
    serializer_class=AssigneesSerializer
    queryset=Assignees.objects.all()
   # lookup_field="username"
    