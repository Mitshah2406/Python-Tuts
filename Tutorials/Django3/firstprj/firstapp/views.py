from django.shortcuts import render
from django.http import HttpResponse
from .models import book
# Create your views here.


def index(request):
    book_list = book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'firstapp/index.html', context)


def detail(request, book_id):
    Book = book.objects.get(id = book_id)
    context = {
        'Book_d':Book
    }
    return render(request, 'firstapp/detail.html',context)
