# Generated by Django 4.2.4 on 2023-08-17 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_car_is_electric_car_is_hybrid_car_mileage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer_related',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='demo.manufacturer'),
        ),
    ]