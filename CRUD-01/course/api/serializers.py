from rest_framework import serializers
 
from course.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
      model=User
      fields=['id', 'name', 'email', 'password']