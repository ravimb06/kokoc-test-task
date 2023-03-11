from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Модель пользователей."""
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

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)
