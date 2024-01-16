from rest_framework import serializers
from .models import InternshipRole, InternshipRequest

class InternshipRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipRole
        fields = '__all__'

class InternshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipRequest
        fields = '__all__'