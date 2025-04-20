"""
URL configuration for heart_disease_prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictor.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]