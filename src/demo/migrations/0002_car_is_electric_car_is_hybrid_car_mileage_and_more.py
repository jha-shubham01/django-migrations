# Generated by Django 4.2.4 on 2023-08-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_electric',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='is_hybrid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='num_seats',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
