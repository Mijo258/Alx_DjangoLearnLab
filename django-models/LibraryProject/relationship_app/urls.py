from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth import views as auth_views

# This is a good practice for namespacing your URLs
app_name = 'relationship_app'

urlpatterns = [
    # URL for the Function-Based View (lists ALL books)
    path('books/', views.list_books, name='list_books'),

    # URL for the Class-Based View (shows ONE library's details)
    # The <int:pk> part is CRITICAL. It captures the library's ID from the URL.
    # e.g., /library/1/ will show the library with primary key = 1.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Registration URL (points to your custom view)
    path('register/', views.register, name='register'),
    
    # Login URL (uses Django's built-in view)
    # We tell it which template to use.
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout URL (uses Django's built-in view)
    # We tell it which template to show after logging out.
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('dashboard/admin/', views.admin_view, name='admin_view'),
    path('dashboard/librarian/', views.librarian_view, name='librarian_view'),
    path('dashboard/member/', views.member_view, name='member_view'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', views.book_delete, name='book_delete'),
]