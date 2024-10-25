from rest_framework.views import APIView
from rest_framework.response import Response
from myapp import models 
from .serializers import StudentSerializer,TeacherSerializer

class TopperListView(APIView):
    def get(self, request):
        toppers = models.Student.objects.order_by('-percentage')[:2]  # Get the top 2 students based on percentage
        serializer = StudentSerializer(toppers, many=True)
        return Response(serializer.data)


def get_students_with_cutoff(cutoff_percentage):
    """Retrieve students who have a percentage above the cutoff."""
    return models.Student.objects.filter(percentage__gte=cutoff_percentage)

def get_students_without_cutoff(cutoff_percentage):
    """Retrieve students who have a percentage below the cutoff."""
    return models.Student.objects.filter(percentage__lt=cutoff_percentage)    

  # Ensure you import the models

def get_teacher_performance():
    """Retrieve the performance data for teachers based on emp_id."""
    passing_threshold = 33.0
    performance_data = []

    # Get all teachers
    teachers = models.Teacher.objects.all()
    for teacher in teachers:
        students = models.Student.objects.filter(emp_id=teacher)  # Filter by emp_id
        total_students = students.count()
        total_passed = students.filter(percentage__gte=passing_threshold).count()

        passing_percentage = (total_passed / total_students * 100) if total_students > 0 else 0

        performance_data.append({
            "emp_id": teacher.emp_id,
            "passing_percentage": passing_percentage,
            "total_passed": total_passed,
            "total_students": total_students
        })
    
    return performance_data

