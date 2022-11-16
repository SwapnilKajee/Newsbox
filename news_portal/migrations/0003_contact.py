# Generated by Django 4.1.1 on 2022-10-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0002_alter_news_options_rename_views_news_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
