from django.contrib import admin
from django.contrib.admin import AdminSite
from studreg.models import Student

# Register your models here.
# admin.site.register(Student)  # Imports a data model and registers it

class StudentAdmin(admin.ModelAdmin):
    """For super admin"""
    
    list_display = ('entrance_roll_no', 'admission_no', 'name', 'tc_taken')
    # list_filter = ('tc_taken',) # Enable to add a filter to the admin page 
    search_fields = ['entrance_roll_no', 'admission_no']  # Adds a search box to the admin page
    save_on_top = True

admin.site.register(Student, StudentAdmin)
