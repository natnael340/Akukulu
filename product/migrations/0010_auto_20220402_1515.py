# Generated by Django 2.2.12 on 2022-04-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20220401_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
