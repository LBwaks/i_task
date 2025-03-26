from rest_framework import serializers
from .models import Task, Sector, Source, Issue, Support,Status,Priority,TaskFiles,TaskComment
from django.contrib.auth.models import User
from Accounts.serializers import UserSerializer
from Accounts.models import Assignees

user=UserSerializer()

class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Sector
        fields = ['sector_name', 'description']


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Source
        fields = ['user', 'source_name', 'description']
class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Issue
        fields = ['user', 'issue_type', 'description']
class SupportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Support
        fields = ['user', 'support_name', 'description']

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = [#'users', 
                  'status_name', 'description']   

class PrioritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Priority
        fields = ['user', 'priority_type', 'description']      

class TaskFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model =TaskFiles
        fields =['task','file']        




class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail',lookup_field='slug')
    created_by = serializers.HyperlinkedRelatedField(view_name='user-detail',lookup_field='username',queryset=User.objects.all() )
    #created_by=  UserSerializer()
    # assigned_to= UserSerializer()
    file = TaskFileSerializer(many=True,required=False)
    task_files =serializers.ListField(child=serializers.FileField(allow_empty_file = True,use_url=False),write_only=True,required=False)
    class Meta:
        model = Task
        fields = ['url', 'created_by',
                  'sector',
                 'source','issue_type',
                  'customer_id',
                'title','description',
                'support_type','status','priority',
                'start_date','end_date',
                'file',                
               'assigned_to','task_files',
                'create_date', 
                'update_date']
        
        def validate():
            pass

        def create(self ,validated_data):
            task_files =validated_data.pop("task_files",[])
            task = Task.object.create(**validated_data)
            for file in task_files:
                TaskFiles.objects.create(task=task,file=file)
            return task



# def validate

# TaskComment
class TaskCommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='taskcomment-detail')
    task = serializers.HyperlinkedRelatedField(view_name='task-detail',lookup_field='slug',queryset=Task.objects.all())
    user = serializers.HyperlinkedRelatedField(view_name='user-detail',lookup_field='username',queryset=User.objects.all())

    class Meta:
        model =TaskComment
        fields = ['url','task','user','comment','create_date','update_date']


