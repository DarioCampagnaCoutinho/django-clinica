from django.urls import path, include
from core.views import home

urlpatterns = [
    path('home', home, name='home'),
]
