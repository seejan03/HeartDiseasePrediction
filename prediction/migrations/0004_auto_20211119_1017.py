# Generated by Django 3.0.2 on 2021-11-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0003_auto_20211119_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='trestps',
            field=models.IntegerField(),
        ),
    ]