from django.db import models
from users.models import BaseModel
from urls_items.models import Url
from django import forms

class Result(BaseModel):

    url = models.ForeignKey(
        Url,
        on_delete=models.CASCADE,
        verbose_name="Url associé",
        db_index=True,
        null=False,
        blank=False,
        default=None
    )

    success = models.BooleanField(
        verbose_name="Succès",
        default=None,
        blank=False,
        null=False,
    )

    http_code = models.TextField(
        verbose_name="Code HTTP",
        default=None,
        blank=True,
        null=True,
    )

    has_text = models.BooleanField(
        verbose_name="Présence de texte sur la page",
        default=None,
        blank=True,
        null=True,
    )

    answer_delay = models.TextField(
        verbose_name="Temps de réponse",
        default=None,
        blank=True,
        null=True,
    )

    ssl_certificat_validation = models.BooleanField(
        verbose_name="Validation du certificat SSL",
        default=None,
        blank=False,
        null=True,
    )

    ssl_delay_before = models.IntegerField(
        verbose_name="Délai avant expiration",
        default=None,
        blank=True,
        null=True,
    )

    date = models.DateTimeField(
        verbose_name="Date et heure de la vérification",
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.url.url

    class Meta:
        verbose_name = "Résultats suite a l'appel http"
        verbose_name_plural = "Résultats suite aux appels http"