# Generated by Django 5.1.5 on 2025-02-11 00:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposttranslation',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
