# Generated by Django 3.1.1 on 2020-09-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0003_auto_20200906_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniquelinks',
            name='fired',
            field=models.BooleanField(default=False),
        ),
    ]
