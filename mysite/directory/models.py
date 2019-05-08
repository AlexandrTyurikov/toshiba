from django.db import models
from django.urls import reverse_lazy


class Author(models.Model):
    name = models.CharField('Автор(ы)', max_length=120)
    description = models.TextField('Автобиография', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('author_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Series(models.Model):
    name = models.CharField('Серия', max_length=120)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('series_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=120)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('genre_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publishing(models.Model):
    name = models.CharField('Издательство', max_length=120)
    description = models.CharField('Город', max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('publishing_dv', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
