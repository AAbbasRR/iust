from django.contrib.auth.models import AbstractUser, BaseUserManager, update_last_login
from django.db import models, transaction
from django.utils.translation import gettext as _

from utils import BaseErrors


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def register_user(self, email=None, password=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        if not password:
            raise ValueError(BaseErrors.user_must_have_password)
        with transaction.atomic():
            user = self.create_user(email, password)
        return user

    def find_by_email(self, email=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        return self.filter(email=email).first()


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email'),
        max_length=256,
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name=_('Is Active'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def activate(self):
        """
        :return: active user account after email account validate
        """
        with transaction.atomic():
            self.is_active = True
            self.save()
        return self

    def set_last_login(self):
        """
        :return: When the user logs in, we record her login time as the last login time
        """
        update_last_login(None, self)
        return self
