# Generated by Django 3.0.5 on 2020-05-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200503_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
