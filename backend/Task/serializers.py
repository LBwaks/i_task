from rest_framework import serializers
from .models import Task, Sector, Source, Issue, Support,Status,Priority,TaskFiles
from django.contrib.auth.models import User
from Accounts.serializers import UserSerializer


class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Sector
        fields = ['sector_name', 'description']


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Source
        fields = ['users', 'source_name', 'description']
class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Issue
        fields = ['users', 'issue_type', 'description']
class SupportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Support
        fields = ['users', 'support_name', 'description']
class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Status
        fields = ['users', 'status_name', 'description']   

class PrioritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        Model = Priority
        fields = ['users', 'priority_type', 'description']      

class TaskFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model =TaskFiles
        fields =['task','file']        


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='task-detail',lookup_field='slug')
    # user=  UserSerializer()
    # assigned_to= UserSerializer()
    file = TaskFileSerializer(many=True,required=False)
    image_files =serializers.ListField(child=serializers.ImageField(),write_only=True,required=False)
    class Meta:
        model = Task
        fields = ['url', #'user',
                  'sector',
                 'source','issue_type',
                  'customer_id',
                'title','description',
                'support_type','status','priority',
                'start_date','end_date',
                'file',
                'image_files',
              #  'assigned_to',
                'create_date', 
                'update_date']
        
        def validate():
            pass


# def validate


