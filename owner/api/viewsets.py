from rest_framework import viewsets

from owner.api import serializers
from owner import models


class OwnerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OwnerSerializer
    queryset = models.Owner.objects.all()