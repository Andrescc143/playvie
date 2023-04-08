# Generated by Django 4.1.7 on 2023-04-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_playlist_movie_playlists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='playlists',
        ),
        migrations.AddField(
            model_name='playlist',
            name='movies',
            field=models.ManyToManyField(to='movie.movie'),
        ),
    ]
