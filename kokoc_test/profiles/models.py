from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    """Модель пользователей."""
    RED = '#f2100c'
    BLUE = '#0000FF'
    ORANGE = '#FFA500'
    GREEN = '#008000'
    PURPLE = '#800080'
    GOLDEN = '#ccc01f'

    COLOR_CHOICES = [
        (RED, 'Красный'),
        (BLUE, 'Синий'),
        (ORANGE, 'Оранжевый'),
        (GREEN, 'Зеленый'),
        (PURPLE, 'Фиолетовый'),
        (GOLDEN, 'Золотой'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия',
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='email',
    )
    scores = models.IntegerField(
        default=0,
        verbose_name="Колличество очков",
    )
    coins = models.IntegerField(
        default=0,
        verbose_name="Колличество монет",
    )
    background_color = models.CharField(
        max_length=7,
        choices=COLOR_CHOICES,
        verbose_name='код цвета логина'
    )

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('scores',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)
