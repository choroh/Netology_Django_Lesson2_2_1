# Generated by Django 4.0 on 2021-12-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
