from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from djaein_core import BaseManager, BaseModel


class UserManager(BaseUserManager, BaseManager):

    def create_superuser(self,
                         email,
                         password):
        user = self.model(email=email, is_superuser=True, is_staff=True)
        user.set_password(password)
        user.save()
        user = self.get(email=user.email)
        return user


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
    is_staff = models.BooleanField(
        verbose_name='Staff Status',
        default=False,
        help_text='Identify whether the user is a staff or not.',
    )

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return str(self.email)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user_users'
