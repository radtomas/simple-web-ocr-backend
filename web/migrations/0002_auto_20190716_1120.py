# Generated by Django 2.2.3 on 2019-07-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='origin_url',
        ),
        migrations.AddField(
            model_name='image',
            name='encoded_file',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.TextField(default=''),
        ),
    ]