# Generated by Django 4.2.7 on 2023-11-22 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_feed_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='feed.feed'),
        ),
    ]
