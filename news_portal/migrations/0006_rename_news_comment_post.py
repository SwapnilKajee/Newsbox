# Generated by Django 4.1.1 on 2022-10-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='news',
            new_name='post',
        ),
    ]
