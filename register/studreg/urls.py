from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # To test a view
]