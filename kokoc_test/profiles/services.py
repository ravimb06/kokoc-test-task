from .models import Profile
from django.db.models import F


def scoring_profile_add(profile: Profile, scores, coins):
    """Функция для добавления очков и монет за тест."""
    profile.update(scores = F("scores") + scores)
    profile.update(coins = F("coins") + coins)


def scoring_profile_remove_coins(profile: Profile, coins):
    """Функция для уменьшения монет после покупки."""
    profile.update(coins = F("coins") + coins)
