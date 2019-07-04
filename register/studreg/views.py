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
    num_stud_took_tc = Student.objects.filter(tc_taken__exact=True).count() # Number of students who took TC from GECBH

    context = {
        'num_stud' : num_stud,
        'num_stud_took_tc' : num_stud_took_tc,
    }

    return render(request, 'index.html', context=context)

