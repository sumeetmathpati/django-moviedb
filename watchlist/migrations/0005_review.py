# Generated by Django 3.2.9 on 2021-11-02 02:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0004_media_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('media', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='watchlist.media')),
            ],
        ),
    ]
