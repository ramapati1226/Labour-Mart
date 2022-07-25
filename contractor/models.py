from django.db import models
from django.core.validators import RegexValidator
class contractor_detail(models.Model):
    contractor_id = models.AutoField
    contractor_name = models.CharField(max_length=50)
    contractor_city = models.CharField(max_length=300)
    contractor_dob = models.DateField(auto_now=False, auto_now_add=False)
    contractor_email = models.EmailField()
    contractor_mob = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contractor_jobdetails = models.CharField(max_length=500)
    contractor_state = models.CharField(max_length=50)
    pub_date = models.DateField()