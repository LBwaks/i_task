from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='tasks',
        lookup_field='slug'
    )
    
    class Meta:
        model = Task
        fields = ['sector', 'user','source','issue_type','customer_id'
                'title','description','support_type','status','priority'
                'start_date','end_date','assigned_to','create_date', 
                'update_date']
        
        def validate():
            pass


# def validate
