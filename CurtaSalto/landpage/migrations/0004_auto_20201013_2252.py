# Generated by Django 3.1.1 on 2020-10-13 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0003_auto_20201013_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landpage.tempuserid', unique=True),
        ),
    ]
