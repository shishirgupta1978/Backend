from django.http import HttpResponse
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from core.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer



class ListUsersView(generics.ListCreateAPIView):
    User=get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)