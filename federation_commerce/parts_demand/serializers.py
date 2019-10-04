from rest_framework import serializers
from .models import PartsDemand
from django.contrib.auth.models import User


class PartsDemandSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PartsDemand
        fields = ['id', 'description', 'delivery_addr', 'contact_info', 'owner', 'conclusion_status']


class UserSerializer(serializers.ModelSerializer):
    parts_demand = serializers.PrimaryKeyRelatedField(many=True, queryset=PartsDemand.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'parts_demand']
