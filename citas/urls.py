from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.citas_view, name='citas_view'),
    path('<int:pk>', views.cita_view, name='cita_view'),
]