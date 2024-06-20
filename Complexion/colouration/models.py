from django.db import models

# Create your models here.
class ImageData(models.Model):
    image = models.ImageField(upload_to='your_image')
