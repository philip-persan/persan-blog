from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_('Nome'),
        max_length=100,
        blank=False,
        null=True
    )

    def __str__(self) -> str:
        return self.name
