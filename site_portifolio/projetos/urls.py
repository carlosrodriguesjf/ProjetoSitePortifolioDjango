

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projetos, name ='projetos')
]
