# Generated by Django 3.1.5 on 2021-01-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2m_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='m2m_app.Student'),
        ),
    ]
