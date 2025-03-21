from django.contrib.auth.models import User
from.models import Assignees
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail',lookup_field="username")
        
    class Meta:
        model = User
        fields = ['id', 'url', 'username']
        #extra_kwargs = {'url': {'lookup_field': 'username'}} 

class AssigneesSerializer(serializers.HyperlinkedModelSerializer):
    assignee = serializers.HyperlinkedRelatedField(view_name="user-detail",lookup_field="username",queryset=User.objects.all() )
   # created_by = serializers.HyperlinkedRelatedField(view_name="user-detail",lookup_field="username",queryset=User.objects.all() )
   # url =serializers.HyperlinkedIdentityField(view_name='assignees-detail',lookup_field="username")
    class Meta:
        model= Assignees
        fields = [#'created_by',
                  'url','assignee','update_date']