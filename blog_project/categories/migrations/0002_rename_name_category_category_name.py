# Generated by Django 5.0.2 on 2024-06-14 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='Category_name',
        ),
    ]
