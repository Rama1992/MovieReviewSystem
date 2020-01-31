# Generated by Django 3.0.2 on 2020-01-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesreviewsystem', '0009_auto_20200129_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewers',
            name='viewer_rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)'),
        ),
    ]
