from django.db import models
from users.models import BaseModel

class Url(BaseModel):
    
    name = models.CharField(
        verbose_name = "Nom de l'url",
        max_length = 100,
        blank=False,
        null=False,
    )

    url = models.CharField(
        verbose_name="url à appeler",
        max_length=255,
        blank=False,
        null=False,
        default=None
    )

    def __str__(self):
        return self.name