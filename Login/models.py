from django.db import models
from django.contrib.auth.models import User,AbstractUser,BaseUserManager

class NewUserManager(BaseUserManager):
    def create_user(self, email, phone, password, **kwargs):
        try:
            email = self.normalize_email(email)
            user = self.model(email=email,phone=phone, **kwargs)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)


    def create_superuser(self,email,phone,password, **kwargs):
        # norm_email = self.normalize_email(email)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        return self.create_user(email, phone, password, **kwargs)

class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    objects = NewUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    def __str__(self):
        return self.email

