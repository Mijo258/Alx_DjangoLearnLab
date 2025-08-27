from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.http import HttpResponse
from django.views import listview, DetailView

def list_books(request):
    # the output should be a list of all books and their authors
    books = Book.objects.all()
    output = ', '.join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output)


class librarylistview(listview):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
class librarydetailview(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


# Create your views here.
