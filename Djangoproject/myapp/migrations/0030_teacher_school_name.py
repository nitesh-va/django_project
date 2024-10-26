# Generated by Django 5.1.2 on 2024-10-25 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_student_dept_name'),
        ('school', '0002_school_created_on_school_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='school_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='school.school'),
        ),
    ]
