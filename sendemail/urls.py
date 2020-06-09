from django.contrib import admin
from django.urls import path

from .views import contactView, SuccessView

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('success/', SuccessView, name='success'),
]