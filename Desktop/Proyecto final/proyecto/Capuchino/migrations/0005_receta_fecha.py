# Generated by Django 4.1.3 on 2023-01-02 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capuchino', '0004_receta_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
