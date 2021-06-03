from django.db import models
# from model_utils.models import TimeStampedModel
from django_extensions.db.models import TimeStampedModel
import users.models

class Category(TimeStampedModel):
    name = models.CharField(max_length = 300)

class Product(TimeStampedModel):
    user = models.ForeignKey(users.models.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "category")