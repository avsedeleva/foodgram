# Generated by Django 3.2.6 on 2021-08-06 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210806_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество'),
        ),
    ]
