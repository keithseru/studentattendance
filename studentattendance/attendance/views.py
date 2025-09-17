from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def homePage(request):
    attendanceList = Student.objects.order_by('student_id')
    
    #Counting the attendance
    present = 0
    absent = 0
    
    for student in attendanceList:
        if student.is_present:
            present += 1
        else:
            absent += 1
    
    context = {
        'attendanceList' : attendanceList,
        'present': present,
        'absent': absent,
    }
    return render(request, 'index.html', context)

def createPage(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        student_id = request.POST.get("student_id")
        date = request.POST.get("date")
        is_present_str = request.POST.get("is_present")
        
        #Convert str to Boolean
        if is_present_str == "true":
            is_present = True
        else:
            is_present = False
        
        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            student_id = student_id,
            date = date,
            is_present = is_present
        )    
        
        return redirect("home")
    
    return render(request, 'create.html')

def viewSingleStudent(request, student_id):
    selected_student = Student.objects.get(id=student_id)
    context = {
        'student' : selected_student
    }
    return render(request, 'view.html', context)

def updateSingleStudent(request, student_id):
    selected_student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        selected_student.first_name = request.POST.get("first_name")
        selected_student.last_name = request.POST.get("last_name")
        selected_student.student_id = request.POST.get("student_id")
        selected_student.date = request.POST.get("date")
        
        is_present_str = request.POST.get("is_present")
        if is_present_str == 'true':
            selected_student.is_present = True
        else:
            selected_student.is_present = False
        
        selected_student.save()
        return redirect("home")
    
    context = {
        'student' : selected_student
    }
    return render(request, 'update.html', context)

def deleteSingleStudent(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect("home")
    
    context = {
        'student': student
    }
    
    return render(request, 'delete.html', context)