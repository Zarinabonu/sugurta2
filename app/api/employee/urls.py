from django.urls import path

from app.api.employee import views

urlpatterns = [
    path('list', views.EmployeeListAPIView.as_view(), name='employee_list'),
]