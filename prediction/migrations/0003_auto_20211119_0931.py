# Generated by Django 3.0.2 on 2021-11-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_auto_20211118_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='exang',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='oldpeak',
            field=models.FloatField(),
        ),
    ]
