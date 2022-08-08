from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    UZ = "uz"
    RU = "ru"
    EN = "en"

    LANGUAGES = ((UZ, UZ), (RU, RU), (EN, EN))

    languages = models.CharField(choices=LANGUAGES, default=UZ, max_length=25)
    birthday = models.DateField(null=True)
    about = models.CharField(max_length=255, null=True)
    is_new = models.BooleanField(default=True)
