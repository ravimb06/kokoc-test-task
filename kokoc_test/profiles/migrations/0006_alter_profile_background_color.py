# Generated by Django 4.1.7 on 2023-03-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0005_alter_profile_background_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="background_color",
            field=models.CharField(
                choices=[
                    ("color:#f2100c", "Красный"),
                    ("color:#0000FF", "Синий"),
                    ("color:#FFA500", "Оранжевый"),
                    ("color:#008000", "Зеленый"),
                    ("color:#800080", "Фиолетовый"),
                    ("color:#ccc01f", "Золотой"),
                ],
                default="color:#008000",
                max_length=16,
                verbose_name="код цвета логина",
            ),
        ),
    ]
