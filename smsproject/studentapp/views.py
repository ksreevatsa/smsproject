from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course
from facultyapp.models import CourseContent

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]
    flag = Student.objects.filter(Q(studentid=sid) & Q(password=pwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["sid"] = sid  # creating session variable (auname)
        student = Student.objects.get(studentid=sid)
        print(student)
        return render(request, "studenthome.html", {"sid": sid,"student":student})

    else:
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"message": msg})


# Create your views here.
def studenthome(request):
    sid = request.session["sid"]
    student=Student.objects.get(studentid=sid)
    print(student)
    return render(request,"studenthome.html",{"sid":sid,"student":student})

def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        Student.objects.filter(studentid=sid).update(password=npwd)
        msg="Password Updated Successfully"
    else:
        msg ="Old Password is Incorrect"
    return render(request,"studentchangepwd.html",{"sid":sid,"message":msg})

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request, "studentchangepwd.html",{"sid":sid})

def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def displaystudentcourses(request):
    sid = request.session["sid"]
    ay=request.POST["ay"]
    sem=request.POST["sem"]

    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request,"displaystudentcourses.html", {"courses": courses,"sid":sid})


def studentcoursecontent(request):
    sid = request.session["sid"]
    content = CourseContent.objects.all()
    return render(request,"studentcoursecontent.html", {"sid":sid,"coursecontent":content})

