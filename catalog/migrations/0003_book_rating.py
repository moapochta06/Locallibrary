# Generated by Django 5.0.7 on 2024-11-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_author_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Rate this book from 1.00 to 5.00', max_digits=3, null=True),
        ),
    ]
