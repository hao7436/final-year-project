# Generated by Django 3.0.3 on 2022-08-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiScam', '0010_addactivites_activitesdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='addactivites',
            name='toDo1',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='addactivites',
            name='toDo2',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='addactivites',
            name='toDo3',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
