# Generated by Django 3.1.5 on 2021-01-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('m2m_app', '0003_auto_20210111_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField()),
                ('final_grade', models.CharField(blank=True, max_length=1, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_app.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m2m_app.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='m2m_app.Enrollment', to='m2m_app.Student'),
        ),
    ]
