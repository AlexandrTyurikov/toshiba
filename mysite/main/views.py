from django.views.generic import ListView
from django.db.models import Q
from book.models import Book
from cart.views import CountInCart


class BookCard(CountInCart, ListView):
    model = Book
    template_name = 'main/mainPage.html'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('nnn', False)
        if search != 0:                                # Поиск по названию книги и автору   а это убирает дубли
            return qs.filter(Q(name__icontains=search) | Q(author__name__icontains=search)).distinct()
        return qs
