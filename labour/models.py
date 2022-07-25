from django.db import models
from django.core.validators import RegexValidator
class labour_detail(models.Model):


    labour_id = models.AutoField
    labour_name = models.CharField(max_length=50)
    labour_city = models.CharField(max_length=300)
    labour_dob = models.DateField(auto_now=False, auto_now_add=False)
    labour_email = models.EmailField()
    labour_mob = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    labour_specification = models.CharField(max_length=500)
    labour_state = models.CharField(max_length=50)
    image = models.ImageField(upload_to='labour/images', default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.labour_name