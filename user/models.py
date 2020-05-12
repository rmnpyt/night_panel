from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class user(models.Model):
    user_id = models.AutoField(primery_key=True)
    fullname = models.CharField(max_lenght=500)
    email = models.EmailField(max_lenght=250)
    mobile = models.PhoneNumberField(blank=True)
