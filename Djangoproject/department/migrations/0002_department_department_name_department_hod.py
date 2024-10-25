# Generated by Django 5.1.2 on 2024-10-24 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        ('myapp', '0025_remove_student_class_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='hod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.teacher'),
        ),
    ]