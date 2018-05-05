from django.db import models

# Create your models here.


class Images(models.Model):
    """class to hold the photos"""
    photo = models.ImageField(upload_to='Images/', null=True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()


class Location(models.Model):
    """ class to indicate where the image was taken"""
    name = models.CharField(max_length=30)


class Tag(models.Model):
    """ class to indicate the category of the image"""
    name = models.CharField(max_length=30)
