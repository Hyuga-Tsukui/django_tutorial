# Generated by Django 3.1.1 on 2020-09-04 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Choise', 'Choice')
    ]
