from django import forms
from .models import Faculty,Student

#AddFacultyForm will be created based on Faculty model
class AddFacultyForm(forms.ModelForm):
        class Meta:
            model=Faculty  #model name
            fields="__all__" #all fields in model,auto feild will be hided
            exclude={"password"} #this will exclude fields
            labels = {"facultyid":"Enter Faculty ID","gender":"Select Gender","fullname":"Enter Full Name"} #to change label name


class AddStudentForm(forms.ModelForm):
    class Meta:
        model =Student # model name
        fields = "__all__"  # all fields in model,auto feild will be hided
        exclude = {"password"}  # this will exclude fields
        labels = {"studentid": "Enter Student ID", "gender": "Select Gender",
                  "fullname": "Enter Full Name"}  # to change label name

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"studentid"}
