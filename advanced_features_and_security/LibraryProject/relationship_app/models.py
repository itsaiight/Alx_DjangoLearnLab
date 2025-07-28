from django.db import models
from django.conf import settings



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
            ("can_add", "Can add a book")
            ("can_change", "Can change a book")
            ("can_delete", "Can delete a book")
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


