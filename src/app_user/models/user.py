from django.contrib.auth.models import AbstractUser, BaseUserManager, update_last_login
from django.db import models, transaction
from django.utils.translation import gettext as _

from utils import BaseErrors


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, *args, **kwargs):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        user = self.model(email=self.normalize_email(email), **kwargs)
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
        user.is_active = True
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
        user.is_active = True
        user.save(using=self._db)
        return user

    def register_user(self, email=None, password=None, agent=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        if not password:
            raise ValueError(BaseErrors.user_must_have_password)
        with transaction.atomic():
            user = self.create_user(email, password, agent=agent)
        return user

    def find_by_email(self, email=None):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        return self.filter(email=email).first()

    def find_admin_by_email(self, email):
        if not email:
            raise ValueError(BaseErrors.user_must_have_email)
        return self.filter(email=email, is_staff=True, is_active=True).first()


class User(AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-id"]

    class AdminOptions(models.TextChoices):
        Nothing = "nothing"
        Prof = "prof"
        Staff = "staff"
        Karshenas = "karshenas"

    first_name = None
    last_name = None
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    sub = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_("Sub Code")
    )
    picurl = models.CharField(
        max_length=125, null=True, blank=True, verbose_name=_("Picture URL")
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email"),
        max_length=256,
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name=_("Is Active"),
    )
    agent = models.EmailField(null=True, blank=True, verbose_name=_("Agent Email"))
    admin_role = models.CharField(
        max_length=9,
        choices=AdminOptions.choices,
        default=AdminOptions.Nothing,
        verbose_name=_("Admin Role"),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.id} {self.username} {self.email}"

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

    def change_password(self, new_pass):
        """
        :return: update user password
        """
        with transaction.atomic():
            self.set_password(new_pass)
            self.save()
        return self
