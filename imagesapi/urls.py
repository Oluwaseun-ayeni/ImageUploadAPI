from . import views 
from rest_framework.routers import SimpleRouter
from django.urls import path, include


app_name = 'imagesapi'

router = SimpleRouter()
router.register('product', views.ProductViewSet)
router.register('image', views.ImageViewSet)


urlpatterns = [
    path('', include(router.urls))
]