# Generated by Django 5.0.2 on 2024-04-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_evaluacion_materia_alter_evaluacion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='materia',
            field=models.CharField(max_length=100),
        ),
    ]
