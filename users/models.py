from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created       = models.DateTimeField(auto_now_add = True, verbose_name="Date de création")
    modified      = models.DateTimeField(auto_now = True, verbose_name="Date de modification")

    class Meta:
        abstract = True
        ordering = ("-created", )