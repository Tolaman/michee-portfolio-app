from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
     class Meta:
          model = Contact
          fields = '__all__'
          read_only_fields = ('created_at',) # Exclude created_at from write operations