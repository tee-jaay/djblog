# Generated by Django 2.0.3 on 2018-03-16 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_author_profile_pircute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='profile_pircute',
            new_name='profile_picture',
        ),
    ]
