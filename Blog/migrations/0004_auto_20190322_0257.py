# Generated by Django 2.1.7 on 2019-03-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_allblogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allblogs',
            name='image',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
