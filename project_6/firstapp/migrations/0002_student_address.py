# Generated by Django 5.0.2 on 2024-06-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='jamalpur'),
        ),
    ]
