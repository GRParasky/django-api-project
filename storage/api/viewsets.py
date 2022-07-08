from rest_framework import viewsets

from storage.api import serializers
from storage.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        title = self.request.query_params.get('title')
        price = self.request.query_params.get('price')

        if title is not None:
            queryset = queryset.filter(title=title)
        elif price is not None:
            queryset = queryset.filter(price=price)
        elif title is not None and price is not None:
            queryset = queryset.filter(title=title, price=price)

        return queryset
