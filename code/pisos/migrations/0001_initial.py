# Generated by Django 5.1.3 on 2024-11-11 16:23

import pisos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to=pisos.models.file_location)),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
    ]