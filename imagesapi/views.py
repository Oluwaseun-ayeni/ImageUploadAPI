from .serializer import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet
from .models import Image,Product

class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ProductViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Product.objects.all()

