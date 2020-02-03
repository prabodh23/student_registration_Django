from django.shortcuts import render
from django.views import View
# Create your views here.


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import EmpData, studentData
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class StaffLogin(View):  # login class
    def get(self, request, *args, **kwargs):  # if request is get
        return render(request, "vimeet/stafflogin.html")

    def post(self, request, *args, **kwargs):  # if request is post
        uname = request.POST.get('username')
        password = request.POST.get('password')
        # print(uname,password)
        staff = authenticate(request, username=uname, password=password)
        if staff:
            login(request, staff)
            # print(uname,password)
            return redirect(EmpReg)  # redirect page to home page or registration page
        else:
            return render(request, "vimeet/stafflogin.html", {'error': "Wrong username or password"})
            # return same page if invalid credential


@login_required(login_url="StaffLogin")  # decorator foruser is login or not
def EmpReg(request):  # Showing registration page
    return render(request, "vimeet/registration.html")

@login_required(login_url="StaffLogin")  # decorator foruser is login or not
def showStudData(request):  # Showing registration page
    all_Emp_data = EmpData.objects.all()
    SerNo = len(all_Emp_data)
    return render(request, "vimeet/EmployeesData.html", {'Emp_savedData': all_Emp_data, 'serno': SerNo})


def studReg(request):  # Showing registration page
    return render(request, "vimeet/registration.html")


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class DisplayEmpData(LoginRequiredMixin, View):
    # print(user.username)
    login_url = "StaffLogin"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):  # for displaying employee detail from database get request
        # print("HHHHHHHHH")
        all_Emp_data = EmpData.objects.all()
        SerNo = len(all_Emp_data)
        # return all employee data which will be stored till now
        return render(request, "vimeet/EmployeesData.html", {'Emp_savedData': all_Emp_data, 'serno': SerNo})


class DisplayStudData(LoginRequiredMixin, View):
    # print(user.username)
    login_url = "StaffLogin"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):  # for displaying employee detail from database get request
        # print("HHHHHHHHH")
        all_stud_data = studentData.objects.all()
        SerNo = len(all_stud_data)
        # return all employee data which will be stored till now
        return render(request, "vimeet/StudentData.html", {'Stud_savedData': all_stud_data, 'serno': SerNo})


class SaveEmpData(View):  # for saving employee data into database
    # if (request.method=='POST'):
    def post(self, request, *args, **kwargs):  # save data if request is post
        try:
            empName = request.POST.get('emp_name', 'NA')
            emailadd = request.POST.get('email', 'NA')
            phoneNo = request.POST.get('mob_no', '00')
            department = request.POST.get('department', 'NA')
            if (request.POST.get('department', 'NA') == ""):
                department = "NA"
            print(empName,emailadd,phoneNo,department)
            obj = EmpData(Emp_name=empName, Emp_email=emailadd, Emp_phonNO=phoneNo,
                          Emp_dept=department)  # database object
            obj.save()
            return redirect("empData")

        except Exception as e:
            print(e)
            return HttpResponse("Try again")

    def get(self, request, *args, **kwargs):  # get request
        return redirect("EmpReg")


class saveStudData(View):  # for saving employee data into database
    # if (request.method=='POST'):
    def post(self, request, *args, **kwargs):  # save data if request is post
        try:
            studName = request.POST.get('firstname', 'NA')
            studLast = request.POST.get('lastname', 'NA')
            country = request.POST.get('country', 'NA')
            subject = request.POST.get('subject', 'NA')
            if (request.POST.get('department', 'NA') == ""):
                department = "NA"
            print(studName, studLast, country, subject)
            obj = studentData(stud_name=studName, stud_last=studLast, stud_country=country,
                          stud_subject=subject)  # database object
            obj.save()
            return HttpResponse("Your details are successfully stored, We will consider you.. Thank you..!")

        except Exception as e:
            print(e)
            return HttpResponse("Try again")

    def get(self, request, *args, **kwargs):  # get request
        return redirect("studReg")

@login_required(login_url="StaffLogin")  # decorator
def logout1(request):  # for logout
    logout(request)
    return redirect("StaffLogin")

def home_page(request) :                           #Showing registration page
    return render(request,"vimeet/index.html")

def contact_us(request) :                           #Showing registration page
    return render(request,"vimeet/response_form.html")

def login_page(request) :                           #Showing registration page
    return render(request,"vimeet/login_page.html")