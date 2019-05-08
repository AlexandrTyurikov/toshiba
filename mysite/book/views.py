from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import SearchActiveForm, BookCrUpForm
from django.db.models import Q


class BookDetail(DetailView):
    model = Book


class BookList(ListView):
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


class BookCreate(CreateView):
    model = Book
    form_class = BookCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('book_lv')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('book_lv')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_lv')
    template_name = 'form/delete_form.html'
