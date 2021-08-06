from django.urls import path

from app.api.handbook import views

urlpatterns = [
    path('currency/list', views.CurrencyListAPIView.as_view(), name='currency_list'),
    path('city/list', views.CityListAPIView.as_view(), name='city_list'),
]