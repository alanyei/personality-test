from django.urls import path

from . import views

urlpatterns = [
    path('', views.apt_index, name='index'),
]
