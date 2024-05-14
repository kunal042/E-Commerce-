from django.urls import path
from flipapp import views

urlpatterns = [
    path("", views.home, name='home')
]