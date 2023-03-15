from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    """Модель пользователей."""
    RED = 'color:#f2100c'
    BLUE = 'color:#0000FF'
    ORANGE = 'color:#FFA500'
    GREEN = 'color:#008000'
    PURPLE = 'color:#800080'
    GOLDEN = 'color:#ccc01f'

    COLOR_CHOICES = [
        (RED, 'Красный'),
        (BLUE, 'Синий'),
        (ORANGE, 'Оранжевый'),
        (GREEN, 'Зеленый'),
        (PURPLE, 'Фиолетовый'),
        (GOLDEN, 'Золотой'),
    ]
    id = models.IntegerField(primary_key=True)
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
    tests_taken = models.IntegerField(
        default=0,
        verbose_name="количество пройденых тестов",
    )
    scores = models.IntegerField(
        default=0,
        verbose_name="количество очков",
    )
    coins = models.IntegerField(
        default=0,
        verbose_name="количество монет",
    )
    background_color = models.CharField(
        max_length=16,
        choices=COLOR_CHOICES,
        default=GREEN,
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
