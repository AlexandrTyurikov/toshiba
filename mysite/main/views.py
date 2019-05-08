from django.views.generic import ListView
from book.models import Book
from django.db.models import Q


class BookCard(ListView):
    model = Book
    template_name = 'main/mainPage.html'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('nnn', False)
        if search != 0:                                  # Поиск по названию книги и автору
            return qs.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        return qs
