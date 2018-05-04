from django.db import models

# Create your models here.


class Images(models.Model):
    """class to hold the photos"""
    photo = models.ImageField(upload_to='Images/', null=True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
