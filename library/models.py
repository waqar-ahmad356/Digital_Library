from django.db import models  # Importing the Django models module
from django.contrib.auth.models import User  # Importing the User model from Django's built-in authentication system

# Create your models here.

# Defining a Django model called 'Book'
class Book(models.Model):
    # Defining fields for the 'Book' model

    # 'title' field to store the title of the book as a character field (up to 255 characters)
    title = models.CharField(max_length=255)

    # 'author' field to store the author's name as a character field (up to 255 characters)
    author = models.CharField(max_length=255)

    # 'description' field to store the book's description as a text field
    description = models.TextField()

    # 'available' field to store whether the book is currently available for borrowing as a boolean
    available = models.BooleanField(default=True)

    # A human-readable string representation of the 'Book' object, which will be used in admin views
    def __str__(self):
        return self.title

# Defining another Django model called 'BorrowRecord'
class BorrowRecord(models.Model):
    # 'user' field to store a reference to a User object who borrowed the book
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 'book' field to store a reference to the Book object that was borrowed
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # 'borrowed_date' field to store the date and time when the book was borrowed (auto-generated)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    # 'return_date' field to store the date and time when the book was returned (nullable and blank)
    return_date = models.DateTimeField(null=True, blank=True)
