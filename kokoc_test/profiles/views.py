from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from profiles.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('quiz:index_page')
    template_name = 'profiles/signup.html'


class LogIn(FormView):
    success_url = reverse_lazy('quiz:index_page')
    template_name = 'profiles/login.html'