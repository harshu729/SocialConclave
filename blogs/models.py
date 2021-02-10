from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=2000000000,blank=True)
    slug = models.CharField(max_length=2000000000,blank=True)
    time = models.DateTimeField(default=timezone.localtime)
    
    def __str__(self):
        return self.title + f' [{self.time}]'