from django.db import models
from django import utils

GENDER_CHOICES = [
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("OTHER", "Other")
]

POSITION_CHOICES = [
    ("DRIVER", "Driver"),
    ("MECHANICAL ENGINEER", "Mechanical Engineer"),
    ("RECEPTIONIST", "Receptionist")
]


# Create your models here.
class Staff(models.Model):
    regno = models.CharField(verbose_name="Registration Number", max_length=50, blank = False, null=False)
    fname = models.CharField(verbose_name="First name", max_length=30)
    mname = models.CharField(verbose_name="Middle  name", max_length=30)
    sname = models.CharField(verbose_name="Sir name", max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    dob = models.DateField(verbose_name="Date of Birth")
    nati_id = models.IntegerField(verbose_name="National ID")
    phone = models.IntegerField(verbose_name="Phone Number")
    email = models.EmailField()
    position = models.CharField(verbose_name="Position", choices=POSITION_CHOICES, max_length=20)
    dor = models.DateField(verbose_name="Date of Registration", default = utils.timezone.now, blank = True, null = True)

    def __str__(self):
        return str(self.regno)
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staffs"
