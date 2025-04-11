from django.urls import path
from . import views

urlpatterns = [
    path('', views.pradinis, name='pradinis'),
]

#
# from django.urls import path
# from .views import BookListView, BookDetailView, BookCreateView
#
# urlpatterns = [
#     path('books/', BookListView.as_view(), name='book_list'),
#     path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
#     path('books/prideti/', BookCreateView.as_view(), name='book_create'),
# ]