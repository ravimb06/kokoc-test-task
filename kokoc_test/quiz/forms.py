from django import forms


class ProfileColorForm(forms.Form):
    """Форма выбора цвета логина пользователя."""

    colors = forms.ChoiceField(
        choices=[
            ("color:#f2100c", "Красный"),
            ("color:#0000FF", "Синий"),
            ("color:#FFA500", "Оранжевый"),
            ("color:#008000", "Зеленый"),
            ("color:#800080", "Фиолетовый"),
            ("color:#ccc01f", "Золотой"),
        ]
    )
