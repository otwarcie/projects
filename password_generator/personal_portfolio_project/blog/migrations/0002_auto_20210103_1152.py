# Generated by Django 3.1.4 on 2021-01-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]