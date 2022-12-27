from django.db import models
from django.utils.translation import gettext_lazy as _

from author.models import Author
from tag.models import Tag


class Post(models.Model):
    author = models.ForeignKey(
        Author,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=150,
        blank=False,
        null=True
    )
    tag = models.ManyToManyField(
        Tag,
        blank=False,
        verbose_name=_("Tag")
    )
    body = models.TextField(
        verbose_name=_("Body"),
        blank=False,
        null=True
    )
    date_created = models.DateField(
        verbose_name=_("Date Created"),
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Post's")
        ordering = ['-date_created', ]
