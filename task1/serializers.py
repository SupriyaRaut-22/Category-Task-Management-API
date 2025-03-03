from rest_framework import serializers
from .models import Task1

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task1
        fields = '__all__'