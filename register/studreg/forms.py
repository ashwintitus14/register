from django import forms

from .models import Student

class NewStudentForm(forms.ModelForm):
    #Add validation functions
    
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['admission_no']
        

        #labels = {'due_back': _('New renewal date')} #To override labels
        #help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')} #To override help_texts
