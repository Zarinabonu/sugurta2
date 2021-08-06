from rest_framework.generics import ListAPIView

from app.api.employee.serializers import EmployeeListSerializer
from app.model import Employee


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()