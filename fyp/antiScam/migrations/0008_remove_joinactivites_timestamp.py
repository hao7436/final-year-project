# Generated by Django 3.0.3 on 2022-08-10 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antiScam', '0007_joinactivites_joinerdob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinactivites',
            name='timestamp',
        ),
    ]
