from django.urls import path, include

urlpatterns = [
    path('portfolio/', include('app.api.portfolio.urls')),
    path('class/', include('app.api.class_type.urls')),
    path('employee/', include('app.api.employee.urls')),
    path('handbook/', include('app.api.handbook.urls')),
]