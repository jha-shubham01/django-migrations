# Generated by Django 4.2.4 on 2023-08-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(choices=[('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Ford', 'Ford'), ('BMW', 'Bmw'), ('Other', 'Other')], default='Other', max_length=20)),
                ('model_name', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('engine_capacity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
