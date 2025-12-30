from django.urls import path
from . import views # so that it takes from the current folder as the name is generic


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]