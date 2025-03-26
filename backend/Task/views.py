from django.shortcuts import render
from rest_framework import generics,viewsets,status
from .serializers import TaskSerializer,SectorSerializer,SourceSerializer,IssueSerializer,SupportSerializer,IssueSerializer,SupportSerializer,StatusSerializer,PrioritySerializer,TaskCommentSerializer
from .models import Task, Sector,Source,Issue,Support,Status,Priority,TaskComment
from Accounts.models import Assignees
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field='slug'
    parser_classes =[MultiPartParser,FormParser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)
    
    @action(detail=True,methods=['patch'],name='change_assignee')
    def change_asignee(self,request,slug=None):
        ass_obj = self.get_object()
        serializer = TaskSerializer(ass_obj,data=request.data,partial=True,context={"request":request})

        if serializer.is_valid():
            ass_obj.save()
            return Response({"status":"Asignee Change"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'],name='change_status')
    def change_status(self,request,slug=None):
        status_obj=self.get_object()
        serializer=TaskSerializer(status_obj,data=request.data,partial=True,context={"request":request})
        
        if serializer.is_valid():
            #status_obj.change_status(serializer.validated_data["status"])
            status_obj.save()
            return Response({'status':'Status Updated'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True,methods=['POST','GET','DELETE'],name='task_comments')
    def task_comment(self,request,slug=None):
        task_obj =self.get_object()

        #get
        if request.method =='GET':
             comments =task_obj.comments.all()        
             serializer =TaskCommentSerializer(comments,many=True,context={"request":request})
             return Response(serializer.data)
        
        #post
        elif request.method=='POST':
            serializer=TaskCommentSerializer(data=request.data,context={"request":request})
            if serializer.is_valid():
                TaskComment.objects.create(task=task_obj,user=self.request.user,comment=serializer.validate_data['comment'])
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        #delete
        elif request.method=="DELETE":
            comment_id =request.data.get("id")
            if not comment_id:
                return Response({"error":"comment_id is required"},status=status.HTTP_400_BAD_REQUEST)
            try:
                comment= TaskComment.objects.get(id=comment_id,task=task_obj,user=self.request.user)
                comment.delete()
                return Response({"message":"Comment delete"},status=status.HTTP_204_NO_CONTENT)
            except TaskComment.DoesNotExist:
                return Response({"message":"Comment Does not exist"},status=status.HTTP_404_NOT_FOUND)



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

class TaskCommentsViewset(viewsets.ModelViewSet):
    serializer_class=TaskCommentSerializer
    queryset=TaskComment.objects.all()








