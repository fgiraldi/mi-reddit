# Generated by Django 2.0.1 on 2018-03-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20180306_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieza',
            name='imagen',
            field=models.ImageField(null=True, upload_to='uploads/piezas_imagenes'),
        ),
    ]
