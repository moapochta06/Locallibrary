from django.db import models
from django.urls import reverse  #Используется для генерации URL-адресов путем изменения шаблонов URL-адресов

import uuid # Required for unique book instances

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('catalog:author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']



class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)



class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g., Science Fiction, French Poetry, etc.)",
        verbose_name='Название жанра'
    )

    class Meta:
        ordering = ['name']  # Order genres alphabetically by name
        verbose_name = 'Жанр'  # Singular form for admin
        verbose_name_plural = 'Жанры'  # Plural form for admin

    def __str__(self):
        return self.name
    
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=True, blank=True,
                                               help_text="Rate this book from 1 to 5")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('catalog:book-detail', args=[self.pk])