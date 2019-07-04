from django.contrib import admin

from studreg.models import Student

# Register your models here.
# admin.site.register(Student)  # Imports a data model and registers it

class StudentAdmin(admin.ModelAdmin):
    list_display = ('entrance_roll_no', 'admission_no', 'name', 'tc_taken')
    # list_filter = ('tc_taken',) # Enable to add a filter to the admin page    

admin.site.register(Student, StudentAdmin)