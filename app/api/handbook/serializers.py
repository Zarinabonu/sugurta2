from rest_framework.serializers import ModelSerializer

from app.model import Currency, City


class CurrencyListSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ('__all__')


class CityListSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')