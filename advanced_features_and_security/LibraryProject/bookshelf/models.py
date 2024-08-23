from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # users/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

# Example model with a foreign key to the custom user
# other_app/models.py
from django.db import models
from django.conf import settings

class ExampleModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # other fields


# bookshelf/models.py
from django.db import models
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_view", _("Can view book")),
            ("can_create", _("Can create book")),
            ("can_edit", _("Can edit book")),
            ("can_delete", _("Can delete book")),
        ]


# bookshelf/models.py
class Book(models.Model):
    # Custom permissions for Book model
    class Meta:
        permissions = [
            ("can_view", _("Can view book")),
            ("can_create", _("Can create book")),
            ("can_edit", _("Can edit book")),
            ("can_delete", _("Can delete book")),
        ]

# bookshelf/views.py
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # View that requires 'can_edit' permission
