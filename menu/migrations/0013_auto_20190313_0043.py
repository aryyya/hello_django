# Generated by Django 2.1.7 on 2019-03-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_teaitem_leaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='punchline',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='teaitem',
            name='punchline',
            field=models.CharField(default='', max_length=64),
        ),
    ]