from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#  Custom User Manager


class UserManager(BaseUserManager):
    def create_user(self, email, username, terms, password=None, password2=None):
        """
        Creates and saves a User with the given email, username, terms and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            terms=terms,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, terms, password=None):
        """
        Creates and saves a superuser with the given email, username, terms and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            terms=terms,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#  Custom User Model


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200, unique=True)
    terms = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followed", blank=True)
    bio = models.TextField(blank=True, default="")
    profile_image = models.ImageField(
        default='default.png', upload_to='avatars')
    cover_image = models.ImageField(default='default.jpg', upload_to='avatars')
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'terms']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
