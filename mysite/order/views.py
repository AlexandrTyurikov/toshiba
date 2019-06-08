from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Order
from .forms import CheckoutOrderForm
from cart.views import CountInCart
from cart.models import Cart, BookInCart


class OrderCheckoutView(CountInCart, CreateView):
    model = Order
    form_class = CheckoutOrderForm
    template_name = 'cart/cart_view.html'

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('order-list', kwargs={'pk': self.object.pk})


class OrderList(CountInCart, LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'order/order_list.html'
    # login_url = '/auth/login'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        current_user = self.request.user
        return qs.filter(user=current_user)


class OrderDelete(CountInCart, LoginRequiredMixin, DeleteView):
    model = Cart
    template_name = 'form/delete_form.html'

    def get_success_url(self):
        #del self.request.session['cart_id']
        return reverse_lazy('order-list', kwargs={'pk': self.object.pk})


class OrderUpdate(CountInCart, LoginRequiredMixin, UpdateView):
    model = Cart
    form_class = CheckoutOrderForm
    template_name = 'order/order_update.html'
