# Generated by Django 4.2.5 on 2023-10-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_proyecto_date_proyecto_imageproj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imageproj',
            field=models.FileField(blank=True, null=True, upload_to='proyectos/'),
        ),
    ]