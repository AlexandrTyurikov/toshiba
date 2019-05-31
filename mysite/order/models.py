from django.db import models
from cart.models import Cart


class OrderStatus(models.Model):
    name = models.CharField('Статус', max_length=120)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, verbose_name='Статус заказа', on_delete=models.PROTECT)
    name = models.CharField('ФИО', max_length=60)
    phone = models.CharField('Контактный телефон', help_text='+375**-***-**-**', max_length=16)
    email = models.EmailField('Электронная почта', null=True, blank=True, help_text='user@mail.com')
    delivery_address = models.TextField('Адрес доставки', null=True, blank=True)
    comments = models.TextField('Дополнительная информация', null=True, blank=True)
    creation_date = models.DateTimeField('Дата и время создания', auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField('Дата и время изменения', auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Заказ № {}, от {}'.format(self.pk, self.creation_date.strftime('%d.%m.%Y'))

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
