from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.teacher_registration, name='employee-registration'),
    path('list', views.teacher_list, name='employee-list'),
    path('load-Region', views.load_Region, name='load-Region'),
]
