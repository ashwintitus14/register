from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Homepage 
    path('new/', views.new_student, name='new_student'), # Form to register new student
    path('success/', views.register_success, name='register_success'),
    


]

"""Name parameter can be used to reverse the mapper. To dynamically create a URL to the resource that the mapper is designed to handle.
    For example we can use the name parameter to link to the home page from any other page by adding this link in a template:
    <a href="{% url 'index' %}">Home</a>.
    """