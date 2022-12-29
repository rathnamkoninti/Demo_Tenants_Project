from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from datetime import date, timedelta
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid
from datetime import datetime
# from aodh_tenants.models import Domain
from django.contrib.postgres.fields import JSONField


class AbstractBaseModel(models.Model):
    """
    Base abstract model, that has `uuid` instead of `id` and includes `created_at`, `updated_at` fields.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField('Created at',default=datetime.now)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'

class User(PermissionsMixin, AbstractBaseUser, AbstractBaseModel):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField('Username', max_length=255, unique=True, validators=[username_validator])
    email = models.EmailField()
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField(
    'staff status',
    default=False,
    help_text='Designates whether the user can log into this admin site.'
    )
    is_superuser = models.BooleanField(
    'superuser status',
    default=False,
    help_text='Designates whether the user can log into this admin site.'
    )
    is_active = models.BooleanField(
    'active user',
    default=True,
    help_text='Designates whether the user can log into this admin site.'
    )


    objects = UserManager()

    USERNAME_FIELD = 'username'

    @property
    def is_django_user(self):
    # btw, all django-users is designed to be able to login into django-admin.
    # Filtering by 'is_staff' will also work
        return self.has_usable_password()()
# Create your models here.
class PublicTable1(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True, blank=True)
  

class PublicTable2(models.Model):
    name  = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True, blank=True)
