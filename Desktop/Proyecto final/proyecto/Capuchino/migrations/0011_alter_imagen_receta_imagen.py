# Generated by Django 4.1.3 on 2023-01-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capuchino', '0010_alter_imagen_receta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen_receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Avatares'),
        ),
    ]
