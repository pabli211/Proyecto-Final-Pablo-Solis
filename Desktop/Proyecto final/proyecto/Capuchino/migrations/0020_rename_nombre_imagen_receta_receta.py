# Generated by Django 4.1.3 on 2023-01-03 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Capuchino', '0019_rename_receta_imagen_receta_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagen_receta',
            old_name='nombre',
            new_name='receta',
        ),
    ]
