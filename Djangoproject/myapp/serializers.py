from rest_framework import serializers
from myapp import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # emp_id=TeacherSerializer(read_only=True)
    class Meta:
        model = models.Student
        fields = '__all__'

