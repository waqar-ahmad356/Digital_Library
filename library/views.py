# Import necessary modules and functions
from django.shortcuts import render, redirect, get_object_or_404
from .models import BorrowRecord, Book
from .forms import BorrowRecordForm, ReturnBookForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader


# Create your views here.

# Book search View
def book_search(request):
    # Get the 'q' parameter from the URL query string, which is the user's search query
    query = request.GET.get('q')

    # Load the 'book_search.html' template using Django's loader
    template = loader.get_template('book_search.html')

    # Check if a search query ('q') is provided
    if query:
        # If a query is provided, filter books that have titles containing the query
        books = Book.objects.filter(title__icontains=query)
    else:
        # If no query is provided, retrieve all books
        books = Book.objects.all()

    # Create a context dictionary containing the 'books' queryset
    context = {
        'books': books,
    }

    # Render the template with the context data and return an HttpResponse
    return HttpResponse(template.render(context, request))


# Book Detail View
def book_detail(request, pk):
    # Get the book with the given primary key (pk) or return a 404 error if not found
    book = get_object_or_404(Book, pk=pk)

    # Load the 'book_detail.html' template using Django's loader
    template = loader.get_template('book_detail.html')

    # Create a context dictionary containing the 'book' object
    context = {
        'book': book,
    }

    # Render the template with the context data and return an HttpResponse
    return HttpResponse(template.render(context, request))


# Borrow Book View
@login_required()
def borrow_book(request, pk):
    # Get the book with the given primary key (pk) or return a 404 error if not found
    book = get_object_or_404(Book, pk=pk)

    # Load the 'borrow_book.html' template using Django's loader
    template = loader.get_template('borrow_book.html')

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            # If the form is valid, create a borrow record but don't save it to the database yet
            borrow_record = form.save(commit=False)
            borrow_record.user = request.user  # Set the user to the currently logged-in user
            borrow_record.book = book  # Set the book being borrowed
            borrow_record.save()  # Save the borrow record to the database
            book.available = False  # Mark the book as unavailable
            book.save()  # Save the book object

            # Redirect to the book detail page for the borrowed book
            return redirect('book_detail', pk=pk)
    else:
        # If the request method is not POST, display an empty form
        form = BorrowRecordForm()

    # Create a context dictionary containing the 'book' object and the 'form' object
    context = {
        'book': book,
        'form': form
    }

    # Render the template with the context data and return an HttpResponse
    return HttpResponse(template.render(context, request))


# Return Book View
@login_required
def return_book(request, pk):
    # Get the borrow record with the given primary key (pk) or return a 404 error if not found
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)

    # Load the 'return_book.html' template using Django's loader
    template = loader.get_template('return_book.html')

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = ReturnBookForm(request.POST, instance=borrow_record)
        if form.is_valid():
            # If the form is valid, save the form data to the database
            form.save()
            borrow_record.book.available = True  # Mark the book as available
            borrow_record.book.save()  # Save the book object
            # Redirect to the book detail page for the returned book
            return redirect('book_detail', pk=borrow_record.book.pk)
    else:
        # If the request method is not POST, display a form with the existing data
        form = ReturnBookForm(instance=borrow_record)

    # Create a context dictionary containing the 'borrow_record' object and the 'form' object
    context = {
        'borrow_record': borrow_record,
        'form': form,
    }

    # Render the template with the context data and return an HttpResponse
    return HttpResponse(template.render(context, request))
