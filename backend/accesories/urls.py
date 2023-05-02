from django.urls import path
from . import views

urlpatterns = [
    path('', views.products),
    path('/offer', views.offer),
]
