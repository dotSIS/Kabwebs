# Generated by Django 3.2.12 on 2022-05-05 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='author',
        ),
    ]
