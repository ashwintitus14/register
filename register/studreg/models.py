from django.db import models

# Create your models here.

class Student(models.Model):
    """Model representing a student."""

    name = models.CharField('Name of candidate (in block letters)', max_length=100)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)

    caste = models.CharField('Caste', max_length=50)
    religion = models.CharField('Religion', max_length=50)
    community = models.CharField('Community', max_length=50)

    permanent_address = models.TextField('Permanent Address')
    present_address = models.TextField('Present Address', help_text='Copy and paste permanent address if they are the same.')
    phone_1 = models.CharField('Phone Number 1', max_length=20, help_text="Don't use spaces in the phone number.")
    phone_2 = models.CharField('Phone Number 2 (optional)', max_length=20, help_text="Don't use spaces in the phone number.", blank=True, null=True)
    email = models.EmailField('Email ID')

    date_of_birth = models.DateField('Date of Birth')

    concession = models.TextField('Nature of Eligibility for fee concession')

    nationality = models.CharField('Nationality', max_length=20, default='Indian')
    state = models.CharField('State', max_length=30)
    district = models.CharField('District', max_length=50)

    GUARDIAN_CHOICES = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Uncle', 'Uncle'),
        ('Aunt', 'Aunt'),
        ('Grandfather', 'Grandfather'),
        ('Grandmother', 'Grandmother'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Other', 'Other'),
    )
    guardian = models.CharField('Guardian', max_length=15)
    g_occupation = models.CharField("Guardian's Occupation", max_length=50)
    g_address = models.TextField("Guardian's Address")
    g_phone = models.CharField("Guardian's Phone Number", max_length=20, help_text="Don't use spaces in the phone number.")
    g_email = models.EmailField("Guardian's Email ID")
    g_relationship = models.CharField("Guardian's relationship with the student. (If 'Other' selected)", blank=True, null=True)

    
