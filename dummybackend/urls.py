from django.urls import path
from . import views

urlpatterns = [
    path('List', views.listAPIView, name = 'listAPI'),
    path('List/data', views.data, name = 'dataAPI'),
]