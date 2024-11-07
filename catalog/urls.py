from django.urls import path
from .views import index, BookListView,BookDetailView,AuthorDetailView,AuthorListView,BBLoginView,BBLogoutView

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('account/login', BBLoginView.as_view(),name='login'),
    path('account/logout', BBLogoutView.as_view(),name='logout'),
    # path('accounts/password_reset', password_reset, name='password_reset'),
    # path('accounts/password_reset/done/',password_reset_done, name='password_reset_done'),
    # path('accounts/reset/<uidb64>/<token>/',password_reset_confirm, name='password_reset_confirm'),
    # path('accounts/reset/done/', password_reset_complete, name='password_reset_complete'),
    path('books/', BookListView.as_view(), name='books'), 
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/',AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

]
