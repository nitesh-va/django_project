# Generated by Django 5.1.2 on 2024-10-25 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_teacher_school_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='school_name',
        ),
    ]