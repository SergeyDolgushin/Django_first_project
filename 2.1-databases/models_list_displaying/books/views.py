from xmlrpc.client import boolean
from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book
from books.converters import PubDateConverter

template = 'books/books_list.html'


def books_view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def get_data(page, converter, paginator):

    if page.has_previous():
        index = page.previous_page_number()
    else:
        index = 1
    previous_data = converter.to_url(paginator.object_list[index-1].pub_date)
    if page.has_next():
        index = page.next_page_number()
    else:
        index = paginator.num_pages
    next_data = converter.to_url(paginator.object_list[index-1].pub_date)

    return [previous_data, next_data]


def get_current_page(request, books_by_date, books):

    if len(books_by_date) == 0:
        page_number = int(request.GET.get('page', 1))

    if (request.GET.get('page') == None):
        for i, book in enumerate(books):
            if book in books_by_date:
                page_number = i + 1
    else:
        page_number = int(request.GET.get('page'))

    return page_number


def books_filter(request, date):

    converter = PubDateConverter()
    date = converter.to_python(date)
    books_by_date = Book.objects.filter(pub_date=date)
    books = Book.objects.order_by('pub_date')

    page_number = get_current_page(request, books_by_date, books)

    paginator = Paginator(books, 1)
    page = paginator.get_page(page_number)

    array_data = get_data(page, converter, paginator)

    context = {
        'books': page.object_list,
        'page': page,
        'date': array_data
    }
    return render(request, template, context)
