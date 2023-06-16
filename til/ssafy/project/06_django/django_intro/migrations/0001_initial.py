# Generated by Django 2.1.8 on 2019-04-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('audience', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
