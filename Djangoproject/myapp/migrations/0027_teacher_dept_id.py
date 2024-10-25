# Generated by Django 5.1.2 on 2024-10-24 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_department_created_on_department_updated_on'),
        ('myapp', '0026_student_created_on_student_updated_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='dept_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='department.department'),
        ),
    ]