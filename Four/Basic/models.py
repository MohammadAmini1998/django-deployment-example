from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserPersonalInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
#Additional Story:
    Profile_Link=models.URLField(blank=True)
    Image_Profile=models.ImageField(upload_to='profile_pics',blank=True)

