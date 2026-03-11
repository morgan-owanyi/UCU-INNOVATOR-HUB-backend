from rest_framework import serializers
from .models import Project
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    submitted_by = serializers.StringRelatedField(read_only=True)
    approved_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'