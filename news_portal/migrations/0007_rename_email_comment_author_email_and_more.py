# Generated by Django 4.1.1 on 2022-10-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0006_rename_news_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='author_email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lname',
        ),
        migrations.AddField(
            model_name='comment',
            name='author_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]