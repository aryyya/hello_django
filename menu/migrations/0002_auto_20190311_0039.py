# Generated by Django 2.1.7 on 2019-03-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='order',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='teaitem',
            name='order',
            field=models.IntegerField(default=-1),
        ),
    ]
