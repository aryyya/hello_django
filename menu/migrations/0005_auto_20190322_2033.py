# Generated by Django 2.1.7 on 2019-03-22 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20190322_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fooditem',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='teaitem',
            options={'ordering': ['order']},
        ),
    ]