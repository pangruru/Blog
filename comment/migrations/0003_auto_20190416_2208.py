# Generated by Django 2.1.7 on 2019-04-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190416_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='genre',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
