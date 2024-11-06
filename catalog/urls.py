from django.urls import path
from .views import index, BookListView,BookDetailView,AuthorDetailView,AuthorListView

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'), 
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/',AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
