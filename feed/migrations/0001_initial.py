# Generated by Django 3.0.7 on 2020-07-12 12:28

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    replaces = [('feed', '0001_initial'), ('feed', '0002_auto_20200712_1225')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('feed_url', models.URLField(max_length=256, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=300)),
                ('site_url', models.URLField(max_length=256)),
                ('site_updated', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'feeds',
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrieds', to='feed.Feed')),
                ('author', models.CharField(max_length=200, null=True)),
                ('link', models.URLField( max_length=256)),
                ('published', models.DateTimeField()),
                ('summary', models.TextField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
            ],
            options={
                'verbose_name_plural': 'entries',
                'ordering': ['-added'],
            },
        ),
    ]
