# Generated by Django 3.0.8 on 2020-07-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20200713_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
