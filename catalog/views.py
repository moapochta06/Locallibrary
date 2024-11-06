from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


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


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_count'] = self.get_queryset().count()  # Count of books
        return context

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