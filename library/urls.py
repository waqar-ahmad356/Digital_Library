
# Import necessary functions and classes from Django's URL handling module
from django.urls import path

# Import views from the current module (presumably defined in views.py)
from . import views

# Define a list called urlpatterns that maps URLs to view functions
urlpatterns = [
    # Define a URL pattern for searching books
    path('search/', views.book_search, name='book_search'),

    # Define a URL pattern for viewing the details of a specific book
    # <int:pk> is a URL parameter that will be passed to the view function as 'pk'
    path('detail/<int:pk>/', views.book_detail, name='book_detail'),

    # Define a URL pattern for borrowing a specific book
    # <int:pk> is a URL parameter that will be passed to the view function as 'pk'
    path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),

    # Define a URL pattern for returning a specific book
    # <int:pk> is a URL parameter that will be passed to the view function as 'pk'
    path('return/<int:pk>/', views.return_book, name='return_book'),
]
