from django.shortcuts import render

# Create your views here.
from db_books.models import Author, Book, Publisher


def books_view(requests):
    args = {'books': Book.objects.all()}
    return render(requests, 'books.html', args)


def authors_view(requests):
    args = {'authors': Author.objects.all()}
    return render(requests, 'books.html', args)


def book_details(requests, title):
    book = Book.objects.filter(title=title)
    args = {'title': book.title,
            'date': book.date,
            'author': book.authors,
            'publisher': book.publisher}
    return render(requests, 'books.html', args)


def show_books(requests, author):
    args = Book.objects.filter(author=author)
    return render(requests, 'books.html', args)

