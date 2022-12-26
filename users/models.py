import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name='id',
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Phone',
        blank=True,
        null=True
    )
    profile_img = models.ImageField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
        default='User.png'
    )

    def __str__(self) -> str:
        return self.get_full_name()

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
