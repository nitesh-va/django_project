from django.urls import path
from .views import StudentViews, StudentByIdView, TopperListView,PassedStudentsListView,NotPassedStudentsListview
from .views import AverageMarksSubject,Average,TeacherPerformanceView,PassedFailedStudentsCountView
from .views import TeacherPerformance,TeacherViews,TeacherByIdView

urlpatterns = [
    path('', StudentViews.as_view(),name="list_student"),
    path('students/<int:roll_no>/', StudentByIdView.as_view(), name='student_by_roll_no'), 
    path('toppers/', TopperListView.as_view(), name='topper_list'),
    path('cutoff/',PassedStudentsListView.as_view(),name='passed_students' ),
    path('notcutoff/',NotPassedStudentsListview.as_view(),name='not_passed_students'),
    path('average/', Average.as_view(), name='average'),
    path('averagesubject/', AverageMarksSubject.as_view(), name='average_marks'),
    path('teacheravgmarks/', TeacherPerformanceView.as_view(), name='teacher_performance'),
    path('teacherperformance/', PassedFailedStudentsCountView.as_view(), name='passed_students_count'),

]
urlpatterns+=[
    path('Teacher/', TeacherViews.as_view(), name='teacher_list'),
    path('Top/', TeacherPerformance.as_view(), name='teacher_performance'),
    path('Teacher/<int:emp_id>/', TeacherByIdView.as_view(), name='teacher_detail'),
    
]

