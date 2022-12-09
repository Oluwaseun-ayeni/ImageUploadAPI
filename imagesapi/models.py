from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField





class Image(models.Model):
    name = models.CharField(max_length=255)
    image= VersatileImageField(
        'image',
        upload_to='pictures/',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
   
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    ppoi = PPOIField(
        'Image PPOI'
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ManyToManyField('imagesapi.Image', related_name='products')
    # thumbnail = models.ImageField()
    

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


