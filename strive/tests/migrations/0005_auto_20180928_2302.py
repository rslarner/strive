# Generated by Django 2.0.8 on 2018-09-28 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tests', '0004_auto_20180928_2221'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAnsweredQuestion',
            new_name='UserQuestion',
        ),
    ]
