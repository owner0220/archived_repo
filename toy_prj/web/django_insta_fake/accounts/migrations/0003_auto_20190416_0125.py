# Generated by Django 2.1.8 on 2019-04-16 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190416_0122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='file',
            new_name='profile_image',
        ),
    ]