# Generated by Django 5.1.2 on 2024-10-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_student_class_teachers_alter_student_chemistry_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='percentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='student',
            name='total_marks',
            field=models.IntegerField(default=0),
        ),
    ]
