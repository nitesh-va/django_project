from .views import DepartmentView,DepartmentViewByID
from django.urls import path

urlpatterns = [
    path('', DepartmentView.as_view(), name='department_list'),
    path('<int:dept_id>/', DepartmentView.as_view(), name='department_detail'),
    path('dept/<int:dept_id>/', DepartmentViewByID.as_view(), name='department_detail'),
    
]
