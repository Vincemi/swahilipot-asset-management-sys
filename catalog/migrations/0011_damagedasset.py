# Generated by Django 5.0.7 on 2024-07-28 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_assignedasset'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamagedAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('condition', models.CharField(max_length=20)),
                ('organisation_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_reported', models.DateField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.asset')),
            ],
        ),
    ]