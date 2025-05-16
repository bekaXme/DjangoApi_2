from rest_framework import serializers
from .models import PythonMaterial

class PythonMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonMaterial
        fields = ['id', 'title', 'content', 'created_at', 'level']