from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import TaskSerializer,SectorSerializer,SourceSerializer,IssueSerializer,SupportSerializer,IssueSerializer,SupportSerializer,StatusSerializer,PrioritySerializer
from .models import Task, Sector,Source,Issue,Support,Status,Priority
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class SectorViewSet(viewsets.ModelViewSet):

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()    


class SourceViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Source.objects.all()   


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Issue.objects.all()    


class SupportViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Support.objects.all()   


class StatusViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Status.objects.all()    


class PriorityViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Priority.objects.all()    






