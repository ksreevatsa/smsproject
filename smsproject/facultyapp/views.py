from django.db.models import Q
from django.shortcuts import render, redirect

from adminapp.models import Faculty,FacultyCourseMapping,Course
from .forms import AddCourseContentForm
from .models import CourseContent

# Create your views here.
def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]
    flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=pwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["fid"] = fid  # creating session variable (auname)
        return render(request, "facultyhome.html", {"fid": fid})

    else:
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"message": msg})



def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html", {"fid": fid})

def facultycourses(request):
    fid =request.session["fid"]
    courses = Course.objects.all()

    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        if (course.faculty.facultyid==int(fid)):
            fmcourses.append(course)
    count =len(fmcourses)
    return render (request, "facultycourses.html", {"fid": fid,"fmcourses":fmcourses,"count":count})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        msg="Password Updated Successfully"
    else:
        msg ="Old Password is Incorrect"
    return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request, "facultychangepwd.html",{"fid":fid})

def addcoursecontentform(request):
    fid = request.session["fid"]
    form=AddCourseContentForm() #non paramaterized constructor
    if request.method=="POST":
          form1=AddCourseContentForm(request.POST)
          if form1.is_valid():
              form1.save() # this will save the data in the faculty_table
              message = "Content Added Successfully"
              return render(request, "facultycoursecontent.html", {"msg": message,"form":form,"fid":fid})
          else:
              message = "Failed to add Content"
              return render(request, "facultycoursecontent.html", {"msg": message, "form": form, "fid":fid})
    return render(request,"facultycoursecontent.html",{"form":form,"fid":fid})

