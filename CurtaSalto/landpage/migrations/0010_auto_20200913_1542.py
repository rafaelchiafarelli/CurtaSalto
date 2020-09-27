# Generated by Django 3.1.1 on 2020-09-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0009_auto_20200913_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedddvideo',
            name='category',
            field=models.CharField(blank=True, choices=[('0', 'Alunos Atuais'), ('1', 'Alunos Antigos'), ('2', 'Ór Concour')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='embedddvideo',
            name='location',
            field=models.CharField(blank=True, choices=[('0', 'HomePage'), ('1', 'Webnars'), ('2', 'Mostras')], max_length=25, null=True),
        ),
    ]
