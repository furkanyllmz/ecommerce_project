import uuid
from django.db import models

class Product(models.Model):
    uid         = models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    unique=True,
                  )
    name        = models.CharField(max_length=100)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
