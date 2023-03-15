from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, FormView

from profiles.forms import CreationForm, ChangeForm
from .models import Profile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('quiz:index_page')
    template_name = 'profiles/signup.html'


class Update(UpdateView):
    model = Profile
    form_class = ChangeForm
    success_url = reverse_lazy('profiles:my_account')
    template_name = 'profiles/my_account.html'


class LogIn(FormView):
    success_url = reverse_lazy('quiz:index_page')
    template_name = 'profiles/login.html'


@login_required
def my_account(request):
    profile = request.user
    context = {'profile': profile}
    return render(request, 'profiles/my_account.html', context)