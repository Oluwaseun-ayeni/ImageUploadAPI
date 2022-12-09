from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import *
from rest_flex_fields import FlexFieldsModelSerializer



class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        
        # sizes=[
        #     ('full_size', 'url'),
        #     ('thumbnail', 'thumbnail__100x100'),
        # ]
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'content', 'created','updated','image')
        expandable_fields= {
            'images': (ImageSerializer, {'many':True})
        }
