from django.db import models

# Create your models here.

class Pic(models.Model):
    image = models.ImageField(upload_to = 'my image')
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, null=True)