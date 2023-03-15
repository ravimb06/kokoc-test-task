from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from profiles.forms import ChangeForm, CreationForm, ProfileColorForm

from .models import Profile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("quiz:index_page")
    template_name = "profiles/signup.html"


class Update(UpdateView):
    model = Profile
    form_class = ChangeForm
    success_url = reverse_lazy("profiles:my_account")
    template_name = "profiles/my_account.html"


class LogIn(FormView):
    success_url = reverse_lazy("quiz:index_page")
    template_name = "profiles/login.html"


@login_required
def my_account(request):
    """Функция для отображения личного кабинета и смены цвета логина."""
    profile = request.user
    if request.method == "POST":
        form = ProfileColorForm(request.POST)
        if form.is_valid():
            color = form.cleaned_data["colors"]
            if request.user.coins >= 50:
                Profile.objects.filter(id=request.user.id).update(
                    background_color=color
                )
                Profile.objects.filter(id=request.user.id).update(coins=F("coins") - 50)
                messages.error(request, "Цвет логина успешно изменен.")
            else:
                messages.error(request, "Недостаточно монет.")
    else:
        form = ProfileColorForm()
    return render(
        request, "profiles/my_account.html", {"form": form, "profile": profile}
    )
