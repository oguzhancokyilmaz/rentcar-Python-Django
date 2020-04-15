# Generated by Django 3.0.5 on 2020-04-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('fax', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('smtpserver', models.CharField(max_length=20)),
                ('smtpemail', models.CharField(max_length=20)),
                ('smtppassword', models.CharField(max_length=20)),
                ('smtpport', models.CharField(max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('aboutus', models.TextField()),
                ('references', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
