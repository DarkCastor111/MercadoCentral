# Generated by Django 5.2.1 on 2025-05-21 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
