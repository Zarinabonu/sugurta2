from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.model import General_information, Portfolio, Employee, Object


class General_infoSerializer(ModelSerializer):
    contract_num = serializers.CharField(write_only=True, required=False)
    employee = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = General_information
        fields = ("__all__")
        extra_fields = ['portfolio']

    def create(self, validated_data):
        portfolio = validated_data.pop("portfolio")
        user = User.objects.get(id=validated_data.get("employee"))
        print(user)
        employee = Employee.objects.get(user=user)
        portfolio_new = Portfolio.objects.create(contract_num=validated_data.get("contract_num"), employee=employee)
        contract_num = validated_data.pop("contract_num")
        employee = validated_data.pop("employee")
        general_info = General_information(**validated_data)
        general_info.portfolio = portfolio_new
        general_info.save()
        return general_info


class ObjectSerializer(ModelSerializer):
    contract_num = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Object
        fields = ("__all__")

    def create(self, validated_data):
        contract_num = validated_data.get("contract_num")
        portfolio = Portfolio.objects.get(contract_num=contract_num)
        contract_num = validated_data.pop("contract_num")
        object = Object(**validated_data)
        object.portfolio = portfolio
        object.save()
        return object



