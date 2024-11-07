from django.urls import path
from .views import index, BookListView,BookDetailView,AuthorDetailView,AuthorListView,BBLoginView,BBLogoutView,AuthorCreate,AuthorUpdate,AuthorDelete

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('account/login', BBLoginView.as_view(),name='login'),
    path('account/logout', BBLogoutView.as_view(),name='logout'),
    path('books/', BookListView.as_view(), name='books'), 
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/',AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
]
