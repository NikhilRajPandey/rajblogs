# Generated by Django 2.1.7 on 2019-03-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20190322_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allblogs',
            name='image',
            field=models.FileField(default='', upload_to='blog/media'),
        ),
    ]
