# Generated by Django 5.1.4 on 2024-12-12 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='comments',
            new_name='message',
        ),
    ]