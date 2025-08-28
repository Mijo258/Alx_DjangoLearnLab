from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # You can specify the model if you have a custom user model,
        # but the default User model works fine here.
        # You can also add more fields if needed.
        fields = UserCreationForm.Meta.fields + ('email',)

class BookForm(forms.ModelForm):
    class Meta:
        """Meeta class inside Book Form for the Book model."""
        model = Book
        fields = ['title', 'author', 'publication_year']