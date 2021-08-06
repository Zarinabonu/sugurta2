from rest_framework.generics import ListAPIView

from app.api.class_type.serializers import ClassTypeListSerializer
from app.model import Class_type


class ClassTypeListSerializer(ListAPIView):
    serializer_class = ClassTypeListSerializer
    queryset = Class_type.objects.all()