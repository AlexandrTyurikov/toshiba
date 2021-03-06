from django.db import models
from django.urls import reverse_lazy
from directory.models import Author, Genre, Series, Publishing


class Book(models.Model):
    name = models.CharField('Название книги', max_length=180)
    description = models.TextField('Аннотация', null=True, blank=True)
    image = models.ImageField('Обложка', null=True, blank=True, upload_to='cover')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    author = models.ManyToManyField(Author, related_name='author', verbose_name='Автор')
    genre = models.ManyToManyField(Genre, related_name='genre', verbose_name='Жанр')
    series = models.ForeignKey(Series, related_name='series', null=True, blank=True, verbose_name='Серия',
                               on_delete=models.PROTECT)
    publishing = models.ForeignKey(Publishing, related_name='publishing', verbose_name='Издательство',
                                   on_delete=models.PROTECT)
    year = models.IntegerField('Год издания')
    pages = models.IntegerField('Страниц')
    binding = models.CharField('Переплет', max_length=40)
    format = models.CharField('Формат', max_length=120)
    isbn = models.CharField('ISBN', max_length=40)
    weight = models.CharField('Вес', max_length=10)
    age_limit = models.CharField('Возрастные ограничения', max_length=4)
    sum = models.IntegerField('Количество книг в наличии')
    active = models.BooleanField('Доступна для заказа', default=True)
    rating = models.DecimalField('Рейтинг', max_digits=2, decimal_places=1)
    creation_date = models.DateTimeField('Дата и время создания', auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField('Дата и время изменения', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-name']  # Сортировка
