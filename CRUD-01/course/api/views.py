from django.shortcuts import render
from course.api.serializers import StudentSerializer
from course.models import User
from rest_framework import viewsets
from .mypaginations import mypaginationNumber
#from rest_framework.filters import SearchFilter
#from rest_framework.authentication import  BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = mypaginationNumber
    #filter_backends = [SearchFilter]
    #search_fields = ['name']
    
