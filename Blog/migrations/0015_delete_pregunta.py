# Generated by Django 4.1.1 on 2022-10-19 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_remove_pregunta_nombre_pregunta_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pregunta',
        ),
    ]
