# Generated by Django 2.1.5 on 2019-04-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
