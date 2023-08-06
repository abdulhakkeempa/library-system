from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
  """
  Custom Django User Manager for the Custom User Model Created.
  """
  def create_user(self, email, full_name, password=None, **kwargs):
      if not email:
          raise ValueError("Email not provided")

      user = self.model(
          email = self.normalize_email(email),
          full_name = full_name,
          **kwargs
      )
      user.set_password(password) #hashing and storing the password
      user.save(using = self._db) #saving the user with the database.
      return user

  def create_superuser(self, email, full_name, password=None, **kwargs):
      user = self.create_user(
          email=email,
          password=password,
          full_name = full_name,
          **kwargs
      )
      user.is_admin = True
      user.is_staff = True
      user.is_superuser = True
      user.save(using=self._db)
      return user


class User(AbstractBaseUser,PermissionsMixin):
  """
  Custom Django User Model without Username.
  """
  id = models.AutoField(primary_key=True)
  email = models.EmailField(null=False, max_length=255,unique=True)
  full_name = models.CharField(null=False, max_length=100)
  date_of_birth = models.DateTimeField()
  account_type = models.CharField(null=False, max_length=50)

  is_admin = models.BooleanField(default = False)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['full_name','date_of_birth','account_type']

  objects = UserManager()

  def __str__(self):
      return self.full_name
  
  def has_perm(self, perm, obj = None):
      return self.is_admin

  def has_module_perms(self, app_label):
      return True

