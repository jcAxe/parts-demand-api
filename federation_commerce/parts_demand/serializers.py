from rest_framework import serializers
from .models import PartsDemand


class PartsDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsDemand
        fields = ['id', 'description', 'delivery_addr', 'contact_info', 'announcer', 'status']