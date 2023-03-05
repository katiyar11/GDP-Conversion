from django.urls import path

from . import views


urlpatterns = [
    
    path("usd_data_request", views.usd_data_request, name="usd_data_request"),
    path("usd_conversion_request", views.usd_conversion_request, name="usd_conversion_request"),
]