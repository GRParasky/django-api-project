from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from storage.api import viewsets as storageviewsets
from owner.api import viewsets as ownerviewsets


router = routers.DefaultRouter()

router.register(r'products', storageviewsets.ProductViewSet, "Products")
router.register(r'owners', ownerviewsets.OwnerViewSet, "Owners")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
