from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Student,Faculty,Course,FacultyCourseMapping
from .forms import AddFacultyForm, StudentForm, AddStudentForm


def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})

def logout(request):
    return render(request,"login.html")
def checkadminlogin(request):
    # if request.method=="POST":
        adminuname=request.POST["uname"]
        adminpwd=request.POST["pwd"]
        # data = adminuname + "," + adminpwd
        flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
        print(flag)
        if flag:
            print("login sucess")
            request.session["auname"]=adminuname #creating session variable (auname)
            return render(request,"adminhome.html",{"adminuname":adminuname})
            # return HttpResponse("Login Successfully")
        else:
            # return HttpResponse("Login Failed")
            msg="Login Failed"
            return render(request,"login.html",{"message":msg})
    # if request.method == "GET":
    #     adminuname = request.GET["uname"]
    #     adminpwd = request.GET["pwd"]
    #     data = adminuname + "," + adminpwd

    # return HttpResponse(data)

def viewstudents(request):
    auname = request.session["auname"]
    students=Student.objects.all()
    count=Student.objects.count()
    return render(request,"viewstudents.html",{"studentsdata":students,"count":count,"adminuname":auname})
def viewfaculty(request):
    auname = request.session["auname"]
    faculty =Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})
def viewcourses(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursesdata":courses,"count":count,"adminuname":auname})

def adminstudent(request):
    auname = request.session["auname"]
    auname= request.session["auname"] #retreiving here
    return render(request,"adminstudent.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})
def admincourses(request):
    auname = request.session["auname"]
    return render(request,"admincourses.html",{"adminuname":auname})

def addcourse(request):
    auname = request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})

def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"courses": courses, "count":count})
def insertcourse(request):
    if request.method=="POST":
        dept=request.POST["dept"]
        prog=request.POST["prog"]
        ay=request.POST["ay"]
        sem=request.POST["sem"]
        year=request.POST["year"]
        ccode=request.POST["ccode"]
        ctitle=request.POST["ctitle"]
        ltps= request.POST["ltps"]
        credits = request.POST["credits"]

        course=Course(department=dept, program=prog, academicyear=ay, semester=sem, year=year, coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
        Course.save(course)
        message="Course Added Successfully"
        return render(request,"addcourse.html",{"msg":message})


def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "deletecourse.html", {"coursesdata":courses,"count": count})

def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")
    # return HttpResponse("Course Deleted Successfully")

def addfaculty(request):
    auname = request.session["auname"]
    form=AddFacultyForm() #non paramaterized constructor
    if request.method=="POST":
          form1=AddFacultyForm(request.POST)
          if form1.is_valid():
              form1.save() # this will save the data in the faculty_table
              message = "Faculty Added Successfully"
              return render(request, "addfaculty.html", {"msg": message,"form":form,"adminuname":auname})
          else:
              message = "Failed to add Faculty"
              return render(request, "addfaculty.html", {"msg": message, "form": form, "adminuname": auname})
    return render(request,"addfaculty.html",{"form":form,"adminuname":auname})

def deletefaculty(request):
    faculty = Faculty.objects.all()
    count =Faculty.objects.count()
    return render(request, "deletefaculty.html", {"facultydata":faculty,"count": count})

def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    # return HttpResponse("Faculty Deleted Successfully")
    return redirect("deletefaculty")

def addstudent(request):
    auname = request.session["auname"]
    form=AddStudentForm() #non paramaterized constructor
    if request.method=="POST":
          form1=AddStudentForm(request.POST)
          if form1.is_valid():
              form1.save() # this will save the data in the Student_table
              message = "Student Added Successfully"
              return render(request, "addStudent.html", {"msg": message,"form":form,"adminuname":auname})
          else:
              message = "Failed to add Student"
              return render(request, "addStudent.html", {"msg": message, "form": form, "adminuname": auname})
    return render(request,"addStudent.html",{"form":form,"adminuname":auname})

def deletestudent(request):
    student =Student.objects.all()
    count =Student.objects.count()
    return render(request, "deletestudent.html", {"studentsdata":student,"count": count})

def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    # return HttpResponse("Faculty Deleted Successfully")
    return redirect("deletestudent")

def updatestudent(request):
    auname = request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "updatestudent.html", {"studentsdata":student, "count": count,"adminuname":auname})

def studentupdation(request,sid):
     auname = request.session["auname"]
     student=get_object_or_404(Student,pk=sid)
     if request.method=="POST":
            form=StudentForm(request.POST,instance=student)
            if form.is_valid():
                form.save()
                return HttpResponse("Student Updated Successfully")
            else:
                return HttpResponse("Updation Failed")
     else:
        form = StudentForm(instance=student)
     return render(request, "studentupdated.html", {"form": form,"adminuname":auname})


def facultycoursemapping(request):
    fmcourses=FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses})

def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request, "adminchangepwd.html",{"adminuname":auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        Admin.objects.filter(username=auname).update(password=npwd)
        msg="Password Updated Successfully"
    else:
        msg ="Old Password is Incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"message":msg})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})

def courseupdated(request):
    auname = request.session["auname"]
    cid=request.POST["cid"]
    courseid=int(cid)
    dept = request.POST["dept"]
    prog = request.POST["prog"]
    ay = request.POST["ay"]
    sem = request.POST["sem"]
    year = request.POST["year"]
    ccode = request.POST["ccode"]
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]
    Course.objects.filter(id=courseid).update(department=dept, program=prog, academicyear=ay, semester=sem, year=year, coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
    msg = "Courses Updated Successfully"
    return render(request, "courseupdation.html", {"msg":msg,"auname":auname,"cid":cid})