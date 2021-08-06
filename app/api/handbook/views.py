from rest_framework.generics import ListAPIView

from app.api.handbook.serializers import CurrencyListSerializer, CityListSerializer
from app.model import Currency, City


class CurrencyListAPIView(ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()


class CityListAPIView(ListAPIView):
    serializer_class = CityListSerializer
    queryset = City.objects.all()