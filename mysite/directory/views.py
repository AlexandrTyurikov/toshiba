from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Series, Genre, Publishing
from .forms import AuthorCrUpForm, SeriesCrUpForm, GenreCrUpForm, PublishingCrUpForm
from django.db.models import Q


class AuthorDetail(DetailView):
    model = Author


class SeriesDetail(DetailView):
    model = Series


class GenreDetail(DetailView):
    model = Genre


class PublishingDetail(DetailView):
    model = Publishing


class SearchLV(ListView):

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


class AllDirectoryView(TemplateView):
    template_name = 'directory/all_directory_view.html'


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('author_lv')


class SeriesCreate(CreateView):
    model = Series
    form_class = SeriesCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('series_lv')


class GenreCreate(CreateView):
    model = Genre
    form_class = GenreCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('genre_lv')


class PublishingCreate(CreateView):
    model = Publishing
    form_class = PublishingCrUpForm
    template_name = 'form/create_form.html'

    def get_success_url(self):
        return reverse_lazy('publishing_lv')


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('author_lv')


class SeriesUpdate(UpdateView):
    model = Series
    form_class = SeriesCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('series_lv')


class GenreUpdate(UpdateView):
    model = Genre
    form_class = GenreCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('genre_lv')


class PublishingUpdate(UpdateView):
    model = Publishing
    form_class = PublishingCrUpForm
    template_name = 'form/update_form.html'

    def get_success_url(self):
        return reverse_lazy('publishing_lv')


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author_lv')
    template_name = 'form/delete_form.html'


class SeriesDelete(DeleteView):
    model = Series
    success_url = reverse_lazy('series_lv')
    template_name = 'form/delete_form.html'


class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre_lv')
    template_name = 'form/delete_form.html'


class PublishingDelete(DeleteView):
    model = Publishing
    success_url = reverse_lazy('publishing_lv')
    template_name = 'form/delete_form.html'
