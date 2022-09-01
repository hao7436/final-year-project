# Generated by Django 3.0.3 on 2022-07-22 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiScam', '0004_stories_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='cooperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisationName', models.CharField(blank=True, max_length=256)),
                ('organisationEmail', models.CharField(blank=True, max_length=256)),
                ('personInContact', models.CharField(blank=True, max_length=256)),
                ('ContactNumber', models.CharField(blank=True, max_length=256)),
                ('cooperationDetail', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
