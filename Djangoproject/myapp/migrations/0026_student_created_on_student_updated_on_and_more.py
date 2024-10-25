# Generated by Django 5.1.2 on 2024-10-24 05:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_remove_student_class_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]