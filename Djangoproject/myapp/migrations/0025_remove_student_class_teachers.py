# Generated by Django 5.1.2 on 2024-10-23 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_student_class_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_teachers',
        ),
    ]
