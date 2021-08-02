from django.urls import path, include

urlpatterns = [
    path('portfolio/', include('app.api.portfolio.urls')),
]