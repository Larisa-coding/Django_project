from django.urls import path
from . import_views

urlpatterns = [
    path('new', views.new)
]