# Generated by Django 4.1.7 on 2023-04-07 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('overview', models.TextField()),
                ('poster', models.CharField(max_length=120)),
                ('release', models.DateField()),
                ('language', models.CharField(max_length=15)),
                ('adult', models.BooleanField(blank=True)),
                ('rate', models.DecimalField(decimal_places=1, max_digits=2)),
                ('votes', models.IntegerField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.genre')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
