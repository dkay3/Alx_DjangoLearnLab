from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey relationship

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # ManyToMany relationship

class Profile(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)  # OneToOne relationship
    bio = models.TextField()
