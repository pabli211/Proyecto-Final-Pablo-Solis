# Generated by Django 4.1.3 on 2023-01-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capuchino', '0006_alter_receta_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Avatares'),
        ),
    ]