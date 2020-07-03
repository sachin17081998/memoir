from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

#user model

class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender_choices=(('M','Male'),('F','Female'),('O','Other'))
    gender=models.CharField(max_length=1,choices=gender_choices,blank=False)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username
    
#diary entry model    
class diary(models.Model):
    user_profile=models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='diary')
    text=models.TextField()
    creation_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.creation_date)
    def get_absolute_url(self):
        return reverse( 'dashboard', kwargs={'pk':self.pk})