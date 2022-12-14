# Generated by Django 4.1.1 on 2022-10-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0007_rename_email_comment_author_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='fname',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='lname',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
