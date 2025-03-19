from django.shortcuts import render
from rest_framework import generics,viewsets,status
from .serializers import TaskSerializer,SectorSerializer,SourceSerializer,IssueSerializer,SupportSerializer,IssueSerializer,SupportSerializer,StatusSerializer,PrioritySerializer,AssigneesSerializer
from .models import Task, Sector,Source,Issue,Support,Status,Priority
from Accounts.models import Assignees
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field='slug'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
    
    @action(detail=True,methods=['put'],name='change_assignee')
    def change_asignee(self,request,pk=None):
        task = self.get_object()
        serializer = A;

    @action(detail=True, methods=['patch'],name='change_status')
    def change_status(self,request,pk=None):
        status_obj=self.get_object()
        serializer=TaskSerializer(status_obj,data=request.data,partial=True,context={"request":request})
        
        if serializer.is_valid():
            #status_obj.change_status(serializer.validated_data["status"])
            status_obj.save()
            return Response({'status':'Status Updated'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




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

    serializer_class = StatusSerializer
    queryset = Status.objects.all()    


class PriorityViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Priority.objects.all()    

class AssigneeViewSet(viewsets.ModelViewSet):
    serializer_class=AssigneesSerializer
    queryset=Assignees.objects.all()






