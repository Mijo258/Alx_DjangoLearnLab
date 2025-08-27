from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
path('list_books/', views.list_books, name='list_books'),
path('librarlibrarylistviewy/', views.librarylistview.as_view(), name='library_list'),
path('librarydetailview/', views.librarydetailview.as_view(), name='library_detail'),
path('admin/', admin.site.urls),
]