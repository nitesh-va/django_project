from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp import models
from django.db.models import Avg
from .serializers import StudentSerializer,TeacherSerializer
from .utils import  TopperListView,get_students_with_cutoff,get_students_without_cutoff,get_teacher_performance
# Create your views here.

class StudentViews(APIView):
    def get(self,request):
        students=models.Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
class StudentByIdView(APIView):
    def get(self, request, roll_no):
            student = models.Student.objects.get(roll_no=roll_no)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
    

    def delete(self, request, roll_no):
            student = models.Student.objects.get(roll_no=roll_no)
            student.delete()  # Delete the student instance
            return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content for successful deletion

    def put(self, request,roll_no):
        student=models.Student.objects.get(roll_no=roll_no)
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PassedStudentsListView(APIView):
    def get(self, request):
        cutoff_percentage = 40  # Define your cutoff percentage here
        passed_students = get_students_with_cutoff(cutoff_percentage)  # Get students above the cutoff
        serializer = StudentSerializer(passed_students, many=True)
        return Response(serializer.data)

class NotPassedStudentsListview(APIView):
    def get(self, request):
         cut_percentage=40
         notpassed_students=get_students_without_cutoff(cut_percentage)
         serializer=StudentSerializer(notpassed_students,many=True)
         return Response(serializer.data)

class Average(APIView):
    def get(self, request):
        averages = models.Student.objects.aggregate(
            average_total_marks=Avg('total_marks'),
            average_percentage=Avg('percentage')
        )
        return Response(averages)
    
class AverageMarksSubject(APIView):
    def get(self, request):
        averages = models.Student.objects.aggregate(
            maths=Avg('maths_marks'),
            physics=Avg('physics_marks'),
            chemistry=Avg('chemistry_marks')
        )
        return Response(averages) 

class TeacherPerformanceView(APIView):
    def get(self, request):
        performance = (
            Student.objects
            .values('emp_id__emp_id', 'emp_id__name')  # Group by emp_id and get teacher's name
            .annotate(average_marks=Avg('total_marks'))
            .order_by('-average_marks')
        )
        
        return Response(performance)


from myapp.models import Student  # Make sure to import your models

class PassedFailedStudentsCountView(APIView):
    def get(self, request):
        passing_percentage = 33.0
        
        # Initialize a dictionary to hold results
        results = {}

        # Get all students and categorize them by teacher's emp_id
        for student in Student.objects.all():
            teacher_emp_id = student.emp_id.emp_id  # Accessing emp_id from the ForeignKey

            if teacher_emp_id not in results:
                results[teacher_emp_id] = {
                    'passed': 0,
                    'failed': 0
                }

            if student.percentage >= passing_percentage:
                results[teacher_emp_id]['passed'] += 1
            else:
                results[teacher_emp_id]['failed'] += 1
        
        return Response(results)


               
class TeacherPerformance(APIView):
    def get(self, request):
        return Response(get_teacher_performance())

class TeacherViews(APIView):
    def get(self,request):
        teachers=models.Teacher.objects.all()
        serializer=TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    
class TeacherByIdView(APIView):
    def get(self, request, emp_id):
            teacher = models.Teacher.objects.get(emp_id=emp_id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
    
    def delete(self, request, emp_id):
            teacher = models.Teacher.objects.get(emp_id=emp_id)
            teacher.delete()  # Delete the student instance
            return Response(status=status.HTTP_204_NO_CONTENT)
    

    def put(self, request,emp_id):
        teacher=models.Teacher.objects.get(emp_id=emp_id)
        serializer=TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
