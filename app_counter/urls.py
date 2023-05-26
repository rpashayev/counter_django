from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index),
    path('clear', views.clear),
    path('increase', views.increase),
]