from django.urls import path
from . import views


urlpatterns = [
    path('district', views.add_district, name='district'),
    path('Region', views.add_Region, name='Region'),
    path('Ministry', views.add_Ministry, name='Ministry'),
]
