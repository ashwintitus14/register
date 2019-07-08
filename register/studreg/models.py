from django.db import models
from django.urls import reverse


# Create your models here.

class Student(models.Model):
    """Model representing a student."""
	
    admission_no = models.CharField('Admission Number', max_length=10)
    tc_taken = models.BooleanField('Whether TC taken from GECBH', default=False)
    name = models.CharField('Name of candidate (in block letters)', max_length=100)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)

    caste = models.CharField('Caste', max_length=50, blank=True, null=True)
    religion = models.CharField('Religion', max_length=50, blank=True, null=True)
    community = models.CharField('Community', max_length=50, blank=True, null=True)

    permanent_address = models.TextField('Permanent Address')
    present_address = models.TextField('Present Address')
    phone_1 = models.CharField('Phone Number 1', max_length=20, help_text="Don't use spaces in the phone number.")
    phone_2 = models.CharField('Phone Number 2 (optional)', max_length=20, help_text="Don't use spaces in the phone number.", blank=True, null=True)
    email = models.EmailField('Email ID')

    date_of_birth = models.DateField('Date of Birth (Format: YYYY-MM-DD)', help_text="Enter date exactly as shown above.")

    CONCESSION_CHOICES = (
        ('No eligibility', 'No eligibility'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OEC', 'OEC'),
    )
    concession = models.CharField('Nature of Eligibility for fee concession', max_length=20, choices=CONCESSION_CHOICES, default='No eligibility')

    nationality = models.CharField('Nationality', max_length=20, default='Indian')
    state = models.CharField('State', max_length=50, default='Kerala')
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
    guardian = models.CharField('Guardian', max_length=15, choices=GUARDIAN_CHOICES)
    g_name = models.CharField("Guardian's name", max_length=100)
    g_relationship = models.CharField("Guardian's relationship with the student. (If 'Other' selected)", max_length=20, blank=True, null=True)
    g_occupation = models.CharField("Guardian's Occupation", max_length=50)
    g_address = models.TextField("Guardian's Address")
    g_phone = models.CharField("Guardian's Phone Number", max_length=20, help_text="Don't use spaces in the phone number.")
    g_email = models.EmailField("Guardian's Email ID")
    

    local_guardian_name = models.CharField('Name of Local Guardian', max_length=100)
    local_guardian_address = models.TextField('Address of Local Guardian')

    tc_number = models.CharField('Serial Number of TC produced', max_length=50)
    tc_date = models.DateField('Date of TC produced (Format: YYYY-MM-DD)', help_text="Enter date exactly as shown above.")
    tc_institution = models.CharField('Institution from where TC is issued', max_length=150)

    exam_roll_no = models.CharField('Register number of qualifying exam', max_length=50)

    
    

    date_of_admission = models.DateField('Date of admission (Format: YYYY-MM-DD)', auto_now_add=True, help_text="Enter date exactly as shown above.")

    entrance_roll_no = models.CharField('KEAM Entrance Roll number', max_length=10, primary_key=True, unique=True)
    entrance_rank = models.CharField('KEAM State Merit Rank', max_length=10)
    reservation_rank = models.CharField('Special category/Reservation Rank (if applicable)', max_length=10, blank=True, null=True)

    selection_memo_number = models.CharField('Selection Memo Number', max_length=20) #Check sample
    selection_memo_date = models.DateField('Selection Memo Date (Format: YYYY-MM-DD)', help_text="Enter date exactly as shown above.")
    alloted_college_code = models.CharField('Alloted College Code', max_length=10, default='TRV')
    COURSE_CHOICES = (
        ('BTech', 'BTech'),
        ('MTech', 'MTech'),
        ('PhD', 'PhD'),
    )
    alloted_course_code = models.CharField('Alloted Course Code', max_length=10, choices=COURSE_CHOICES, default='BTech')
    BRANCH_CHOICES = (
        ('CE', 'CE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('IT', 'IT'),
        ('ME', 'ME'),
    )
    alloted_branch_code = models.CharField('Alloted Branch Code', max_length=10, choices=BRANCH_CHOICES)
    reservation_code = models.CharField('Reservation/Special Category Code (if applicable)', max_length=10, blank=True, null=True)

    # Documents submitted
    tc_submitted = models.BooleanField('Transfer Certificate', default=False)
    marklist_submitted = models.BooleanField('Marklist', default=False)
    community_submitted = models.BooleanField('Community Certificate', default=False)
    migration_submitted = models.BooleanField('Migration Certificate (ICSE/CBSE/Diploma)', default=False)

    # Fee details
    fee_concession = models.BooleanField('Fee Concession', default=False, help_text="Tick if eligible")
    amount = models.CharField('Amount (Rs)', max_length=20, default=0)
    bank_receipt_no = models.CharField('Bank Receipt No.', max_length=50, null=True, blank=True)

    time_stamp = models.DateTimeField('Timestamp', auto_now_add = True)

    def __str__(self):
        """String represeting the Student object."""
        return self.entrance_roll_no

    def get_absolute_url(self):
        """Returns the url to access a detailed record for this student."""
        return reverse('student-detail', args=[str(self.entrance_roll_no)]
        )
    
    class Meta:
    	unique_together = ['admission_no', 'entrance_roll_no']
