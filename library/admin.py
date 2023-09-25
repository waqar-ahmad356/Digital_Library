# Import the admin module from the Django package
from django.contrib import admin

# Import the Book and BorrowRecord models from the current application's models.py file
from .models import Book, BorrowRecord

# Register the Book model with the Django admin interface
admin.site.register(Book)

# Register the BorrowRecord model with the Django admin interface
admin.site.register(BorrowRecord)
