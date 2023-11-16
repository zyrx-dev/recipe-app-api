# from django.db import models  # noqa

# # Create your models here.

"""
Database Models.
"""

from django.conf import settings

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Creates, saves and returns a new user."""

        if not email:
            raise ValueError('user must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # self._db is used here to support adding multiple DBs to the project
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates, and returns a new superuser."""

        if not email:
            raise ValueError('superuser must have an email address')
        user = self.create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True
        )
        # OR
        # user.is_staff = True
        # user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Assigining user manager to the model
    objects = UserManager()

    # Defines the default field that we're gonna use for authentication.
    # It overrides the default username field set in the default
    # user model in Django to become email.
    USERNAME_FIELD = 'email'


class Recipe(models.Model):
    """Recipe object."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
