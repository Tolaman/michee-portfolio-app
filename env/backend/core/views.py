from django.shortcuts import render
from rest_framework import viewsets # APIView 
#from rest_framework.response import Response
from .models import Contact
from .serializer import ContactSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contact messages.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Uncomment if you want to customize the response
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)