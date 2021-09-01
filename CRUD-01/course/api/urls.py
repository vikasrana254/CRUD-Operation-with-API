from django.urls import path, include
from rest_framework import routers, urlpatterns
from course.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api/', views.Userviewset, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]