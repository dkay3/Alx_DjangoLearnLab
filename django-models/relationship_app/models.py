from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey relationship

    def __str__(self):
        return self.title

class Library(models.Model):  # Renamed from Publisher to Library
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # ManyToMany relationship

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)  # OneToOne relationship
    bio = models.TextField()

    def __str__(self):
        return self.user.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)  # ForeignKey to Library

    def __str__(self):
        return self.name
