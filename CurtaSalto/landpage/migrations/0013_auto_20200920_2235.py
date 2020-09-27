# Generated by Django 3.1.1 on 2020-09-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0012_auto_20200920_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='acting',
            field=models.CharField(choices=[('0', '0'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='votes',
            name='adaptation',
            field=models.CharField(choices=[('0', '0'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='votes',
            name='art_design',
            field=models.CharField(choices=[('0', '0'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='votes',
            name='photografy',
            field=models.CharField(choices=[('0', '0'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='votes',
            name='picture',
            field=models.CharField(choices=[('0', '0'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='votes',
            name='sound_desing',
            field=models.CharField(choices=[('0', '0'), ('1', '2'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default='0', max_length=100),
        ),
    ]