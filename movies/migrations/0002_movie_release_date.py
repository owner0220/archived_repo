# Generated by Django 2.1.8 on 2019-05-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
