# Generated by Django 2.2.5 on 2020-04-25 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='no_of_item',
        ),
    ]