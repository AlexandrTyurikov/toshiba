from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegistrationForm
from cart.views import CountInCart
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


class UserCreate(CountInCart, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'reg/user_form.html'

    def get_success_url(self):
        self.object.set_password(self.object.password)
        self.object.save()
        return reverse_lazy('login')


class UserLoginView(CountInCart, LoginView):
    template_name = 'registration/login.html'


class UserLogoutView(CountInCart, LogoutView):
    template_name = 'registration/logged_out.html'


class UserPasswordChangeView(CountInCart, PasswordChangeView):
    template_name = 'registration/password_change.html'


class UserPasswordChangeDoneView(CountInCart, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class UserPasswordResetView(CountInCart, PasswordResetView):
    template_name = 'registration/password_reset.html'


class UserPasswordResetDoneView(CountInCart, PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class UserPasswordResetConfirmView(CountInCart, PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'


class UserPasswordResetCompleteView(CountInCart, PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
