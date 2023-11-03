from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib import auth


class Author(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
