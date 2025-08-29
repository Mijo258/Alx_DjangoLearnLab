from django.urls import path
from . import views

urlpatterns = [
    # The names ('book_list_view', etc) should match the redirect in your views
    path('', views.book_list_view, name='book_list_view'),
    path('create/', views.book_create_view, name='book_create_view'),
    path('update/<int:pk>/', views.book_update_view, name='book_update_view'),
    path('delete/<int:pk>/', views.book_delete_view, name='book_delete_view'),
]