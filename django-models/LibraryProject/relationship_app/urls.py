from django.urls import path
from . import views

# This is a good practice for namespacing your URLs
app_name = 'relationship_app'

urlpatterns = [
    # URL for the Function-Based View (lists ALL books)
    path('books/', views.list_books, name='list_books'),

    # URL for the Class-Based View (shows ONE library's details)
    # The <int:pk> part is CRITICAL. It captures the library's ID from the URL.
    # e.g., /library/1/ will show the library with primary key = 1.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]