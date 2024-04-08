from django.shortcuts import render
from .models import StudentDetails

def school_table(request):

# Create your views here.
    StudentDetails = StudentDetails.objects.all()

    return render(request, 'Student.html', {'StudentDetails': StudentDetails})
