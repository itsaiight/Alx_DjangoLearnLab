from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)

    
    class Meta:
        permissions = [
            ("can_create", "Can create a book")
            ("can_view", "Can add a book")
            ("can_edit", "Can change a book")
            ("can_delete", "Can delete a book")
        ]


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password=None):
        user = self._create_user(username, email, password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, default='' ,unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        permissions = [
            ('can_view_profile', 'Can view profile')
            ('can_edit_profile', 'Can edit profile')
        ]


book_ct = ContentType.objects.get_for_model(Book)

# Create Groups
editors, _ = Group.objects.get_or_create(name="Editors")
viewers, _ = Group.objects.get_or_create(name="Viewers")
admins, _ = Group.objects.get_or_create(name="Admins")

# Assign Permissions
can_view = Permission.objects.get(codename='can_view', content_type=book_ct)
can_create = Permission.objects.get(codename='can_create', content_type=book_ct)
can_edit = Permission.objects.get(codename='can_edit', content_type=book_ct)
can_delete = Permission.objects.get(codename='can_delete', content_type=book_ct)

# Assign to groups
editors.permissions.set([can_view, can_create, can_edit])
viewers.permissions.set([can_view])
admins.permissions.set([can_view, can_create, can_edit, can_delete])