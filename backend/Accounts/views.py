from django.shortcuts import render
from .serializers import UserSerializer,AssigneesSerializer
from .models import Assignees
from rest_framework import viewsets
from django.contrib.auth.models import User
# googles
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class AssigneeViewSet(viewsets.ModelViewSet):
    serializer_class=AssigneesSerializer
    queryset=Assignees.objects.all()
   # lookup_field="username"
    
#gogle login 

class GoogleLogin(SocialLoginView):
    adapter_class=GoogleOAuth2Adapter
    callback_url="http://127.0.0.1:3000/"
    client_class =OAuth2Client