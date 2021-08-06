from django.urls import path

from app.api.portfolio import views

urlpatterns = [
    path('general/create', views.GeneralInfoCreateAPIView.as_view(), name='general_create'),
    path('object/create', views.ObjectCreateAPIView.as_view(), name='object_create'),
    path('class/create', views.ObjectCreateAPIView.as_view(), name='object_create'),
]