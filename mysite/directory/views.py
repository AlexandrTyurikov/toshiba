from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Author, Series, Genre, Publishing
from .forms import AuthorCrUpForm, SeriesCrUpForm, GenreCrUpForm, PublishingCrUpForm
from cart.views import CountInCart


class AuthorDetail(CountInCart, DetailView):
    model = Author


class SeriesDetail(CountInCart, DetailView):
    model = Series


class GenreDetail(CountInCart, DetailView):
    model = Genre


class PublishingDetail(CountInCart, DetailView):
    model = Publishing


class SearchLV(CountInCart, ListView):

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('sss', False)
        if search != 0:
            return qs.filter(Q(name__icontains=search))
        return qs


class AuthorList(SearchLV):
    model = Author


class SeriesList(SearchLV):
    model = Series


class GenreList(SearchLV):
    model = Genre


class PublishingList(SearchLV):
    model = Publishing


class AllDirectoryView(CountInCart, TemplateView):
    template_name = 'directory/all_directory_view.html'


class AuthorCreate(CountInCart, CreateView):
    model = Author
    form_class = AuthorCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('author-list')


class SeriesCreate(CountInCart, CreateView):
    model = Series
    form_class = SeriesCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('series-list')


class GenreCreate(CountInCart, CreateView):
    model = Genre
    form_class = GenreCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('genre-list')


class PublishingCreate(CountInCart, CreateView):
    model = Publishing
    form_class = PublishingCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('publishing-list')


class AuthorUpdate(CountInCart, UpdateView):
    model = Author
    form_class = AuthorCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('author-list')


class SeriesUpdate(CountInCart, UpdateView):
    model = Series
    form_class = SeriesCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('series-list')


class GenreUpdate(CountInCart, UpdateView):
    model = Genre
    form_class = GenreCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('genre-list')


class PublishingUpdate(CountInCart, UpdateView):
    model = Publishing
    form_class = PublishingCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('publishing-list')


class AuthorDelete(CountInCart, DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
    template_name = 'form/delete_form.html'


class SeriesDelete(CountInCart, DeleteView):
    model = Series
    success_url = reverse_lazy('series-list')
    template_name = 'form/delete_form.html'


class GenreDelete(CountInCart, DeleteView):
    model = Genre
    success_url = reverse_lazy('genre-list')
    template_name = 'form/delete_form.html'


class PublishingDelete(CountInCart, DeleteView):
    model = Publishing
    success_url = reverse_lazy('publishing-list')
    template_name = 'form/delete_form.html'
