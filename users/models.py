import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **other_fields):
        """Create and save a new user"""
        if not email:
            return ValueError("User must have an email address.")
        user = self.model(
            email=self.normalize_email(email.lower()), username=username, **other_fields
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self.db)
        return user

    def create_superuser(
        self,
        email,
        username,
        password=None,
    ):
        """Create and save a superuser"""
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
