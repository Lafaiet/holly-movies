# Generated by Django 3.2.3 on 2021-05-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_movie_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(blank=True, choices=[['Estonia', 'Estonia'], ['Latvia', 'Latvia']], max_length=50, null=True),
        ),
    ]
