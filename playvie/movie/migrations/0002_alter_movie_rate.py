# Generated by Django 4.2.3 on 2023-12-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]