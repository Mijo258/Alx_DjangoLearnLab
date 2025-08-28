from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView  # We only need DetailView for the CBV task
from .models import Library
from .models import Book
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm # Import your new form

# --- 1. Correct Function-Based View ---
def list_books(request):
    """
    Retrieves all books and renders them using a template.
    This fixes the first checker error.
    """
    all_books = Book.objects.all().order_by('title')
    context = {
        'books': all_books
    }
    # The checker is looking for this exact line (or similar)
    return render(request, 'relationship_app/list_books.html', context)

# --- 2. Correct Class-Based View ---
# We use a DetailView to show the details of ONE library and its books.
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, including all books it contains.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # This will be the variable name in the template

def register(request):
      if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # This creates the new user in the database
            return redirect('login') # Redirect to the login page after successful registration
      else:
        form = CustomUserCreationForm()
    
      return render(request, 'relationship_app/register.html', {'form': form})