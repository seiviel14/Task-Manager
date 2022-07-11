from dataclasses import fields
from rest_framework import serializers
from .models import Task, task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'taskName', 'description')
