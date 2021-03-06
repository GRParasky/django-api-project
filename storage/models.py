from django.db import models
from owner.models import Owner


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner,
                              editable=False,
                              on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True,
                                            editable=False)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    price = models.FloatField()
