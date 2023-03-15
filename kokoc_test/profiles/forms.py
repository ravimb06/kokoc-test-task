from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Profile


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('first_name', 'last_name', 'username', 'email')


class ChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = ('background_color',)


class ProfileColorForm(forms.Form):
    """Форма выбора цвета логина пользователя."""
    colors = forms.ChoiceField(choices=[
        ('color:#f2100c', 'Красный'),
        ('color:#0000FF', 'Синий'),
        ('color:#FFA500', 'Оранжевый'),
        ('color:#008000', 'Зеленый'),
        ('color:#800080', 'Фиолетовый'),
        ('color:#ccc01f', 'Золотой'),
    ])
