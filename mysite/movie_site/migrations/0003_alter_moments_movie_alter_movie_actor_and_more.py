# Generated by Django 5.1.4 on 2024-12-22 09:18

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_site', '0002_actor_actor_name_en_actor_actor_name_ru_actor_bio_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moments',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_moments', to='movie_site.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='actor_movies', to='movie_site.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.ManyToManyField(related_name='movies', to='movie_site.country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('144p', '144p'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p')], max_length=160),
        ),
        migrations.AlterField(
            model_name='movielanguages',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_videos', to='movie_site.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movie_site.movie'),
        ),
    ]
