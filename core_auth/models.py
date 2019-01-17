from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        new_allauth_email = EmailAddress()
        new_allauth_email.user = user
        new_allauth_email.email = email
        new_allauth_email.verified = True
        new_allauth_email.primary = True
        new_allauth_email.save()

        return user


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(_('biography'), max_length=500, blank=True)
    location = models.CharField(_('location'), max_length=30, blank=True)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    avatar_url = models.CharField(_('avatar'), max_length=255, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
