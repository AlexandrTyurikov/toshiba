from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Order
from .forms import CheckoutOrderForm


class OrderCheckoutView(CreateView):
    model = Order
    template_name = 'cart/cart_view.html'
    form_class = CheckoutOrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('main')  # ('orders:success', kwargs={'pk': self.object.pk})
