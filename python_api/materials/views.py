from rest_framework import viewsets, filters
from .models import PythonMaterial
from .serializers import PythonMaterialSerializer

class PythonMaterialViewSet(viewsets.ModelViewSet):
    queryset = PythonMaterial.objects.all()
    serializer_class = PythonMaterialSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'level']
    ordering_fields = ['created_at', 'title']
