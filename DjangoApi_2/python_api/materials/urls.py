from django.urls import path,include
from .views import PythonMaterialViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'materials', PythonMaterialViewSet, basename='pythonmaterial')

urlpatterns = [
    path('', include(router.urls)),
]






