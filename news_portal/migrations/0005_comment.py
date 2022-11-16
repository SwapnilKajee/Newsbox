# Generated by Django 4.1.1 on 2022-10-17 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0004_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news_portal.news')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
