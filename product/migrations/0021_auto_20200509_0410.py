# Generated by Django 3.0.5 on 2020-05-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20200509_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]