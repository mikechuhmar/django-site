from django.urls import path, include
from ecomapp.views import base_view


urlpatterns = [
    path('', base_view, name = 'base'),
]
