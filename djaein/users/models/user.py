from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from djaein_core import BaseManager, BaseModel


class UserManager(BaseUserManager, BaseManager):
    pass


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

    email = models.EmailField(
        verbose_name='Email',
        help_text='Email address of the user.',
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=64,
        help_text='First name of the user.',
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=64,
        help_text='Last name of the user.',
        blank=True,
    )

    def __str__(self):
        return str(self.email)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user_users'
