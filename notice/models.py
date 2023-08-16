from django.db import models

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator


# Create your models here.

class postmodel(models.Model):
   
    title = models.CharField(max_length=100)
    content = models.TextField()
    Professor = models.CharField(max_length=100)
    image=models.ImageField(upload_to='upload/',null=True,blank=True,validators=[FileExtensionValidator(['png','jpg'])])
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title



