from django.urls import path
from . import views

urlpatterns = [
    path('', views.matching_setting_list, name='matching_setting_list'),
]
