# Generated by Django 5.0.2 on 2024-06-22 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='taskAssignDate',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]