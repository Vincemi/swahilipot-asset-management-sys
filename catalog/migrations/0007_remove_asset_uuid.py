# Generated by Django 5.0.7 on 2024-07-26 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_asset_uuid_alter_asset_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='uuid',
        ),
    ]