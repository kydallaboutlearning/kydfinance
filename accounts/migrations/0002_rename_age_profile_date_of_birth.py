# Generated by Django 5.1.5 on 2025-01-26 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Age',
            new_name='date_of_birth',
        ),
    ]
