from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.query_utils import select_related_descend
from board.models import Board
from django.utils import timezone
from django_countries.fields import CountryField


# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('You must enter an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    
    email = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    bio = models.TextField()
    join_date = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=255)
    country = CountryField()
    profile_pic = models.ImageField(upload_to='account/profile_pics', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
