# Generated by Django 3.0.5 on 2020-05-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200504_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='status',
            field=models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]