from django.db import models
from users.models import BaseModel
# from urls_results.models import Result

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

    # result = models.ForeignKey(
    #     Result,
    #     on_delete=models.CASCADE,
    #     verbose_name="Résultat",
    #     db_index=False,
    #     default=None,
    #     null=True,
    #     blank=False,
    # )

    def __str__(self):
        return self.name