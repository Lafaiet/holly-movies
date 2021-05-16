# Generated by Django 3.2.3 on 2021-05-16 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_auto_20210516_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
