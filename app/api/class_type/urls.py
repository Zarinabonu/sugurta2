from django.urls import path

from app.api.class_type import views

urlpatterns = [
    path('list', views.ClassTypeListSerializer.as_view(), name='class_type_list'),
]