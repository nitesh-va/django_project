from django.contrib import admin # type: ignore
from myapp.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
