from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    ctx = {'books': books}
    return render(request, 'book_list.html', ctx)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    ctx = {'book': book}
    return render(request, 'book_detail.html', ctx)


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return HttpResponse("Form is invalid")
    form = BookForm()
    ctx = {'form': form}
    return render(request, 'add_book.html', ctx)
