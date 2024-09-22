from django.db import models
from common.models import BaseModel, Media
from django.contrib.auth.models import AbstractUser
from account.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, BaseModel):
    class AuthType(models.TextChoices):
        GOOGLE = "GOOGLE", _("Google Account")
        FACEBOOK = "FACEBOOK", _("Facebook Account")
        TELEGRAM = "TELEGRAM", _("Telegram Account")
        WITH_PHONE = "WITH PHONE", _("Phone Number")

    username = models.CharField(max_length=123, unique=True, null=True, blank=True)
    birth_date = models.DateField(_("birth_date"), null=True, blank=True)
    photo = models.ForeignKey(
        Media, on_delete=models.SET_NULL, null=True, blank=True
    )
    email = models.EmailField(_("email address"), unique=True, null=True, blank=True)
    phone_number = models.CharField(
        _("phone number"), unique=True, max_length=20, null=True, blank=True
    )
    auth_type = models.CharField(
        _("auth type"), choices=AuthType.choices, max_length=244
    )
    telegram_id = models.CharField(_("telegram id"), max_length=55, null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.phone_number or self.email or self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

