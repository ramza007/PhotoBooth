from django.db import models
import datetime as dt

# Create your models here.


class Location(models.Model):
    """ class to indicate where the image was taken"""
    name = models.CharField(max_length=30)


class Tag(models.Model):
    """ class to indicate the category of the image"""
    name = models.CharField(max_length=30)


class Images(models.Model):
    """class to hold the photos"""
    photo = models.ImageField(upload_to='Images/', null=True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey(Location, on_delete=True)
    tag = models .ForeignKey(
        Tag, on_delete=models.CASCADE, blank=True, null=True)
    time_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """ initialize class"""
        return self.name

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    @classmethod
    def get_images(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            gotten_image_posts : list of image post objects from the database
        '''
        gotten_images = Images.objects.all()
        return gotten_images
