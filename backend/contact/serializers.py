from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    # map camelCase from frontend to snake_case in model
    findOut = serializers.CharField(source='find_out', allow_blank=True)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'reason', 'findOut', 'message']
