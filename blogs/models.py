from django.db import models
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    background = models.ImageField(
        upload_to="gallery", default="", blank=False)
    title = models.CharField(max_length=2000000000,  default="", blank=False)
    content = models.TextField(default="", blank=False)
    image1 = models.ImageField(upload_to="gallery", blank=True)
    quote = models.CharField(max_length=2000000000, blank=True, default="")
    content_2 = models.TextField(blank=True, default="")
    image2 = models.ImageField(upload_to="gallery", blank=True)
    content_3 = models.TextField(blank=True, default="")
    slug = models.CharField(max_length=200, default="", blank=False)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + " : " + self.slug + f' [{self.time}]'
