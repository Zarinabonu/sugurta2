from rest_framework.serializers import ModelSerializer

from app.model import Class_type


class ClassTypeListSerializer(ModelSerializer):
    class Meta:
        model = Class_type
        fields = ('__all__')