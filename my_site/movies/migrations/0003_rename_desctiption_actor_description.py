# Generated by Django 3.2 on 2023-08-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230720_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='desctiption',
            new_name='description',
        ),
    ]
