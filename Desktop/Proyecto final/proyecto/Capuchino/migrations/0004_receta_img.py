# Generated by Django 4.1.3 on 2023-01-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capuchino', '0003_alter_cliente_reseña_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='img',
            field=models.ImageField(blank=True, upload_to='Recetas'),
        ),
    ]
