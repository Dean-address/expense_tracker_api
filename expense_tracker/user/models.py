from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            return ValueError("User must provide an email")

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, password=password, username=username)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    username = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"User {self.email}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
