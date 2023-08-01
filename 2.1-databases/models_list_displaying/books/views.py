from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def books_view_by_date(request, pub_dt):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_dt)
    paginator = Paginator(books, 10)
    page = paginator.get_page(pub_dt)
    context = {
        'books': books,
        'page': page,
        'prev': Book.objects.filter(pub_date__lt=pub_dt).first(),
        #'next': Book.objects.filter(pub_date__gt=pub_dt).first()
    }
    return render(request, template, context)