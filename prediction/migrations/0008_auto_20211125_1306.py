# Generated by Django 3.0.2 on 2021-11-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0007_auto_20211125_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='ca',
            field=models.IntegerField(verbose_name='ca0'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='thalach',
            field=models.IntegerField(verbose_name='thalach'),
        ),
    ]
