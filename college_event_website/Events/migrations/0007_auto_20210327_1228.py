# Generated by Django 3.1.6 on 2021-03-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_auto_20210325_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='12:28:17'),
        ),
    ]
