from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Клиент', blank=True, null=True, on_delete=models.CASCADE)
    creation_date = models.DateTimeField("Дата и время создания", auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField("Дата и время изменения", auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Корзина {}, покупателя {}'.format(self.pk, self.user)

    @property
    def book_in_cart_count(self):
        total = 0
        for book in self.book_in_cart.all():
            total += book.quantity
        return total

    @property
    def total_price(self):
        total = 0
        for book in self.book_in_cart.all():
            total += book.price_total
        return total

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, related_name='book_in_cart', verbose_name='Корзина', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book', verbose_name='Книга', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество', default=1)
    creation_date = models.DateTimeField("Дата и время создания", auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField("Дата и время изменения", auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}шт. {} в корзине'.format(self.quantity, self.book.name)

    @property
    def price(self):
        return self.book.price

    @property
    def price_total(self):
        return self.book.price * self.quantity

    class Meta:
        verbose_name = 'В корзине'
        verbose_name_plural = 'В корзине'
        unique_together = ('cart', 'book')
