# Generated by Django 3.1.4 on 2024-01-11 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='telefon',
        ),
    ]
