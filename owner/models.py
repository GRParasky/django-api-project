from django.db import models


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(editable=False,
                            max_length=255)
