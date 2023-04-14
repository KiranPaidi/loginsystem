from django.shortcuts import render, redirect

from StudentApp.models import City, Course, Student


# Create your views here.
def home(request):
    return None


def addstudent(request):
    Cities=City.objects.all()
    Courses=Course.objects.all()
    return render(request,'addstudent.html',{'Cities':Cities,'Courses':Courses})


def display(request):
    s1=Student()
    s1.fname = request.POST['tbfname']
    s1.lname = request.POST['tblname']
    s1.mobile = request.POST['tbmobile']
    s1.email = request.POST['tbmail']
    s1.city_name = City.objects.get(city_name = request.POST['ddlcity'])
    s1.course =Course.objects.get(course = request.POST['ddlcourse'])
    s1.save()
    return redirect('display')


def displaystudent(request):
    s=Student.objects.all()
    return render(request,'displaystudent.html',{'data':s})


def updatedata(request,id):
    s=Student.objects.get(id=id)
    Cities = City.objects.all()
    Courses = Course.objects.all()
    if request.method == 'POST':
        s1 = Student()
        s1.fname = request.POST['tbfname']
        s1.lname = request.POST['tblname']
        s1.mobile = request.POST['tbmobile']
        s1.email = request.POST['tbmail']
        s1.city_name = City.objects.get(city_name=request.POST['ddlcity'])
        s1.course = Course.objects.get(course=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')
    return render(request,'updatedata.html',{'data':s,'Cities':Cities,'Courses':Courses})


def deletedata(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect('display')