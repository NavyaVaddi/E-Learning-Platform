# Generated by Django 4.0.3 on 2022-03-29 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]
