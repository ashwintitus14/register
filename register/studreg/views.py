from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#def index(request):
#   return HttpResponse("Hello, world!") # Test view

from studreg.models import Student

def index(request):
    """View function for home page of site."""

    # Generate count of registered students

    num_stud = Student.objects.all().count()
    num_stud_took_tc = Student.objects.filter(tc_taken=True).count() # Number of students who took TC from GECBH

    context = {
        'num_stud' : num_stud,
        'num_stud_took_tc' : num_stud_took_tc,
    }

    return render(request, 'index.html', context=context) # render expects to find index.html in register/studreg/templates

from .forms import NewStudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def new_student(request):
    """View function to register a new student"""
    if request.method == 'POST':
        # Create a form and populate it with data from the request (binding):
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save()


        return HttpResponseRedirect(reverse('register_success'))
    
    # If this is a GET (or any other method) create the default form.
    else:
        form = NewStudentForm()

    return render(request, 'new.html', {'form': form})

def register_success(request):
    """View function to show successful registration page."""
    
    return render(request, 'success.html')          
