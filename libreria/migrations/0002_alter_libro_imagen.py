# Generated by Django 5.1.2 on 2024-10-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]