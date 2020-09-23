from django.db import models

class BaseImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='base_images')
