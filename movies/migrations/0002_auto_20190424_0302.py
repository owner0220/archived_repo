# Generated by Django 2.1.8 on 2019-04-24 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='score',
            new_name='val',
        ),
    ]
