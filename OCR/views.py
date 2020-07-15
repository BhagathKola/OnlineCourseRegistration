from django.shortcuts import render
from OCR.models import SchclassModel,StudentModel,studentCourse
from django.shortcuts import redirect
from django.contrib import messages



# Create your views here.
def index(request):
    detail = SchclassModel.objects.all()
    #detail = SchclassModel.objects.all()
    return render(request,"index.html",{"detail":detail})

def adminLogin(request):
    return render(request,"adminlogin.html")


def adminHome(request):
    name = request.POST.get('t1')
    pwd = request.POST.get('t2')
    if name == 'admin' and pwd == 'admin':
          return render(request, 'admin.html')
    else:
         return render(request, 'adminlogin.html', {'error': 'login fail'})


def sclass(request):
   return render(request,"schclass.html")

def savedb(request):
    n = request.POST.get('t1')
    fa = request.POST.get('t2')
    da=request.POST.get('t3')
    t=request.POST.get('t4')
    f=request.POST.get('t5')
    d=request.POST.get('t6')
    print(n,fa,da,t,f,d,)
    try:
       SchclassModel(name=n, faculty=fa, date=da, time=t, fee=f, duration=d).save()
       return render(request, "schclass.html", {'msg': 'saved success'})
    except SchclassModel.DoesNotExist:
       return render(request, 'schclass.html', {'msg': 'not saved'})

def viewall(request):
    data=SchclassModel.objects.all()
    return render(request,'viewall.html',{'data':data})

def update(request):
    num = request.GET.get('no')

    data = SchclassModel.objects.get(id=num)

    return render(request, 'update.html', {'data': data})

def cupdate(request):
    no = request.GET.get('no')
    n = request.POST.get('t1')
    fa = request.POST.get('t2')
    da = request.POST.get('t3')
    ti = request.POST.get('t4')
    f = request.POST.get('t5')
    d = request.POST.get('t6')
    if ti and da:
        SchclassModel.objects.filter(id=no).update(name=n, faculty=fa, date=da, time=ti, fee=f, duration=d)
        messages.success(request, 'updated ')
        return viewall(request)
    else:
        messages.error(request, 'not updated')
        return viewall(request)


def delete(request):
    d=request.GET.get('del')
    SchclassModel.objects.filter(id=d).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewall')

#StudentFunctions

def register(request):
    return render(request,"Sregister.html")

def sreg(request):
    a = request.POST.get("a1")
    b = request.POST.get("a2")
    c = request.POST.get("a3")
    d = request.POST.get("a4")
    StudentModel(name=a, contactno=b, email=c, password=d).save()
    messages.success(request, 'registred successfully')
    return redirect('register')



def slogin(request):
    return render(request,"Slogin.html")


def shome(request):
    na = request.POST.get('a1')
    pa = request.POST.get('a2')
    try:
        sa = StudentModel.objects.get(email=na, password=pa)

        return render(request, "Shome.html", {'name': na})
    except StudentModel.DoesNotExist:
        return render(request, "Slogin.html", {"msg": "login faill"})


def sView(request):
    data = SchclassModel.objects.all()
    return render(request, "Sview.html" , {"data":data})

def enroll(request):

    num = request.GET.get('no')
    sid = request.GET.get('sid')
    try:
        studentCourse.objects.get(sid=sid,cid=num)
        messages.error(request,"Enrolled Already!!")
        return redirect('enroll')
    except studentCourse.DoesNotExist:
        studentCourse(sid=sid, cid=num).save()
        messages.success(request,"Enrolled Successfully")
        return redirect('enroll')


def contact(request):
    return render(request,"contact.html")