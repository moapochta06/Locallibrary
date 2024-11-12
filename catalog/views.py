from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author


def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'main/index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
class BBLoginView(LoginView):
    template_name = 'user/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'user/logged_out.html'

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list' 

    def get_queryset(self):
        queryset = super().get_queryset()
        rating_filter = self.request.GET.get('rating')

        if rating_filter:
            queryset = queryset.filter(rating=rating_filter)

        return queryset.order_by('-rating')

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html' 

    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        return render(
            request,
            'books/book_detail.html',
            context={'book':book_id,}
        )


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors/author.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(author=self.object)  # Получаем книги данного автора
        return context
    

class LibrarianRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(name='Librarians').exists()

class AuthorCreate(LoginRequiredMixin, LibrarianRequiredMixin,CreateView):
    model = Author
    fields = '__all__'
    template_name = 'authors/author_form.html'
    initial = {'date_of_death': '12/10/2016',}

class AuthorUpdate(LoginRequiredMixin, LibrarianRequiredMixin,UpdateView):
    model = Author
    template_name = 'authors/author_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(LoginRequiredMixin, LibrarianRequiredMixin,DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    success_url = reverse_lazy('catalog:authors')  