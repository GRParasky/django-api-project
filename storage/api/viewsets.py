from rest_framework import viewsets

from storage.api import serializers
from storage import models


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
