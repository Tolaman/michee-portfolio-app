from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Service, Experience
from .serializer import ProjectSerializer, ServiceSerializer, ExperienceSerializer

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project details.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer