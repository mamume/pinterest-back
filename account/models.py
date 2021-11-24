from django.contrib.auth import validators
from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.db.models import constraints
from django.utils import timezone
from django_countries.fields import CountryField
from django.contrib.auth.validators import UnicodeUsernameValidator



# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('You must enter an email address')
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
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
    
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, validators=[username_validator])
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(null=True)
    bio = models.TextField(blank=True)
    join_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=255)
    country = CountryField()
    profile_pic = models.ImageField(upload_to='account/profile_pics', null=True, blank=True)
    blocked = models.ManyToManyField('self', null=True, blank=True)

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

class UserFollowing(models.Model):
    user_id = models.ForeignKey('UserProfile', related_name='following', on_delete=models.CASCADE)
    following_user_id = models.ForeignKey('UserProfile', related_name='follower', on_delete=models.CASCADE)
    start_follow = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = models.UniqueConstraint(fields=['user_id', 'following_user_id'], name='unique_followers')
        ordering = ['-start_follow']
    
    def __str__(self):
        return f"{self.user_id} start following {self.following_user_id}"

class UserBlocked(models.Model):
    user_id = models.ForeignKey('UserProfile', related_name='blocking', on_delete=models.CASCADE)
    blocking_user_id = models.ForeignKey('UserProfile', related_name='blocker', on_delete=models.CASCADE)
    blocked = models.DateTimeField(default=timezone.now)
    class Meta:
        constraints = models.UniqueConstraint(fields=['user_id', 'blocking_user_id'], name='uinique_blockers')
        ordering = ['-blocked']

    def __str__(self):
        return f"{self.user_id} blocked {self.blocking_user_id}"

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    sender = models.ManyToManyField('UserProfile', related_name="sender")
    reciever = models.ManyToManyField('UserProfile', related_name="reciever")

    class Meta:
        ordering = ['-created_at']

class Notification(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created_at']