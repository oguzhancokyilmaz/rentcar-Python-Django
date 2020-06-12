# Generated by Django 3.0.5 on 2020-05-06 20:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0014_auto_20200506_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('rate', models.IntegerField(blank=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(blank=True, choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
