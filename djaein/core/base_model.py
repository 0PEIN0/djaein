import uuid

from django.db import models


class BaseModel(models.Model):

    uuid = models.UUIDField(
        verbose_name='Unique Identifier',
        help_text='Unique Identifier.',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        default=True,
        help_text='Active or not.'
    )
    date_created = models.DateTimeField(
        verbose_name='Date Created',
        help_text='Creation date.',
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        verbose_name='Date Updated',
        help_text='Last update date.',
        auto_now=True,
    )

    class Meta:
        abstract = True
