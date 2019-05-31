from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import SearchActiveForm, BookCrUpForm
from .models import Book
from cart.views import CountInCart


class BookDetail(CountInCart, DetailView):
    model = Book


class BookList(CountInCart, ListView):
    model = Book

    def get_queryset(self):
        qs = super().get_queryset()
        active = self.request.GET.get('active', False)
        search = self.request.GET.get('search', False)
        if active:
            qs = qs.filter(active=True)
        if search != 0:
            return qs.filter(Q(name__contains=search))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchActiveForm()
        return context


class BookCreate(CountInCart, CreateView):
    model = Book
    form_class = BookCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('book-list')


class BookUpdate(CountInCart, UpdateView):
    model = Book
    form_class = BookCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('book-list')


class BookDelete(CountInCart, DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'form/delete_form.html'
