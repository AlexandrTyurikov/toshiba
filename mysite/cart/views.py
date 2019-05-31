from django.views.generic import UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from book.models import Book
from .models import Cart, BookInCart
from .forms import AddBookForm
from order.models import OrderStatus
from order.forms import CheckoutOrderForm

new_order_status = OrderStatus.objects.get(pk=2)


class CountInCart:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', '0')
        if cart_id != '0':
            context['cart_count'] = Cart.objects.get(pk=cart_id).book_in_cart_count
        else:
            context['cart_count'] = cart_id
        return context


class AddBookToCart(CountInCart, UpdateView):
    model = BookInCart
    form_class = AddBookForm
    template_name = 'cart/add_book.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        self.request.session['cart_id'] = cart.pk
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            book_in_cart.quantity += 1
            book_in_cart.save()
        return book_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_id'] = self.kwargs.get('pk')
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', '/')


class CartView(DetailView):
    model = Cart
    template_name = 'cart/cart_view.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, cart_created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        # defaults={'user': self.request.user}
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckoutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        checkout_form.fields['status'].initial = new_order_status
        context['form'] = checkout_form
        context['cart_count'] = self.object.book_in_cart_count
        return context


class DeleteFromCart(CountInCart, DeleteView):
    model = BookInCart
    success_url = reverse_lazy('cart-view')
    template_name = 'form/delete_form.html'
