from django.db import models
from users.models import BaseModel

# Create your models here.
class Url(BaseModel):
    name = models.CharField(
        verbose_name = "Nom",
        max_length = 100,
        )

    def __str__(self):
        return self.name