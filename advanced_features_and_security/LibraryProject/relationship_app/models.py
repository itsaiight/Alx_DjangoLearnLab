from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    
    class Meta:
        permissions = [
            ("can_add", "Can add a book"),
            ("can_view", "Can view a book"),
            ("can_create", "Can create a book"),
            ("can_edit", "Can edit a book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField
    library = models.OneToOneField(Library, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')




# Get content type for Book
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