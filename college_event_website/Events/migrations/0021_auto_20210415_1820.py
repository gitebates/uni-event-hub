# Generated by Django 3.1.6 on 2021-04-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0020_auto_20210415_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(blank=True, default='18:20:42'),
        ),
    ]
