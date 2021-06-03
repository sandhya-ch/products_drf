from django.db import models
# from model_utils.models import TimeStampedModel
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser, TimeStampedModel):

    profile_picture = models.ImageField(upload_to='images', null = True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])])
    is_active = models.BooleanField(_('active'), default=True)


    def __str__(self):
        return self.email