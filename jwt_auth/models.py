from django.db import models
from django.contrib.auth.models import AbstractUser

from recipes.models import Recipe
# Create your models here.


class CustomUser(AbstractUser):
    favorites = models.ManyToManyField(Recipe, related_name="liked_by", default=None)

    def __str__(self):
        return f"{self.username}"

