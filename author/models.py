import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Author(models.Model):
    id = models.UUIDField(
        verbose_name='id',
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    user = models.OneToOneField(
        User,
        verbose_name=_("Usuário"),
        on_delete=models.CASCADE
    )
    profissao = models.CharField(
        verbose_name=_('Profissão'),
        max_length=100,
        blank=False,
        null=False,
        default=_('Desenvolvedor')
    )
    nivel_choices = (
        ('JR', 'Junior'),
        ('PL', 'Pleno'),
        ('SR', 'Seinor'),
    )
    nivel = models.CharField(
        verbose_name=_('Nível'),
        max_length=20,
        blank=False,
        null=False,
        default='JR',
        choices=nivel_choices
    )
    sexo = models.CharField(
        verbose_name=_('Sexo'),
        max_length=1,
        blank=False,
        null=False,
        default='M',
        choices=(
            ('F', _('Female')),
            ('M', _('Male')),
            ('N', _('Non Binary')),
        )
    )
    data_nascimento = models.DateField(
        verbose_name=_("Data de Aniversário"),
        auto_created=False,
        blank=True,
        null=True,
    )
    pais = models.CharField(
        verbose_name=_('País'),
        max_length=100,
        blank=True,
        null=True
    )
    estado = models.CharField(
        verbose_name=_('Estado'),
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.user.get_full_name()

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _("Author's")
