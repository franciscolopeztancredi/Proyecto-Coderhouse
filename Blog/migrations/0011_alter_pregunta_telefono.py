# Generated by Django 4.1.1 on 2022-09-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_comentario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='telefono',
            field=models.IntegerField(blank=True),
        ),
    ]