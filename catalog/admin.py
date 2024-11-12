from django.contrib import admindocs
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

class BooksInline(admin.TabularInline):  # из задания 4
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BooksInline]#из задания 4. теперь Администраторы могут добавлять, редактировать или удалять несколько книг, связанных с одним автором, за один раз.
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')#из задания 4
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre','rating')
    inlines = [BooksInstanceInline]  # Чтобы редактировать данные экземпляра книги на странице книги

    def display_genre(self, obj):
        """Возвращает строку с названиями жанров для отображения."""
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])  # Используйте obj для доступа к жанрам
    
    display_genre.short_description = 'Жанр'  # Название столбца в админке
    



# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)