# Generated by Django 2.1.5 on 2019-07-08 01:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studreg', '0010_auto_20190707_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
