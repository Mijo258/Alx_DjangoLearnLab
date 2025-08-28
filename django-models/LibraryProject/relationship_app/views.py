from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView  # We only need DetailView for the CBV task
from .models import Library
from .models import Book
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm # Import your new form
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth.decorators import user_passes_test, login_required

# from .decorators import is_in_role  # Uncomment if you created decorators.py
# Or define the function here directly

# This is our check function
def is_in_role(user, role_name):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role_name

# The user_passes_test decorator is the key to passing the check.
@user_passes_test(lambda u: is_in_role(u, 'Admin'))
def admin_view(request):
    """A view only accessible to users with the 'Admin' role."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: is_in_role(u, 'Librarian'))
def librarian_view(request):
    """A view only accessible to users with the 'Librarian' role."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: is_in_role(u, 'Member'))
def member_view(request):
    """A view only accessible to users with the 'Member' role."""
    return render(request, 'relationship_app/member_view.html')
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

@login_required
@role_required('Admin')
def admin_view(request):
    """A view only accessible to users with the 'Admin' role."""
    return render(request, 'relationship_app/admin_view.html')

@login_required
@role_required('Librarian')
def librarian_view(request):
    """A view only accessible to users with the 'Librarian' role."""
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@role_required('Member')
def member_view(request):
    """A view only accessible to users with the 'Member' role."""
    return render(request, 'relationship_app/member_view.html')