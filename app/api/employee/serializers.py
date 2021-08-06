from rest_framework.serializers import ModelSerializer

from app.model import Employee


class EmployeeListSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')