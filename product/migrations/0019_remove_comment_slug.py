# Generated by Django 3.0.5 on 2020-05-07 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20200508_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
