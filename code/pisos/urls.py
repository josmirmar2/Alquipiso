from django.urls import path
from pisos import views

urlpatterns = [
    path('', views.pisos, name='index'),  # This handles the root URL
    path('pisos/', views.pisos, name='pisos'),
]