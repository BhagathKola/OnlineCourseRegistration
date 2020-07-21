from django.shortcuts import render
from OCR.models import CourseregModel,StudentlogModel,studentCourse
from django.shortcuts import redirect
from django.contrib import messages
from django.db.utils import IntegrityError



# Create your views here.
def index(request):
    detail = CourseregModel.objects.all()
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
       CourseregModel(name=n, faculty=fa, date=da, time=t, fee=f, duration=d).save()
       return render(request, "schclass.html", {'msg': 'Course Registered Successfully'})
    except CourseregModel.DoesNotExist:
       return render(request, 'schclass.html', {'msg': 'not saved'})

def viewall(request):
    data=CourseregModel.objects.all()
    return render(request,'viewall.html',{'data':data})

def update(request):
    num = request.GET.get('no')

    data = CourseregModel.objects.get(cid=num)

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
        CourseregModel.objects.filter(cid=no).update(name=n, faculty=fa, date=da, time=ti, fee=f, duration=d)
        messages.success(request, 'updated ')
        return viewall(request)
    else:
        messages.error(request, 'not updated')
        return viewall(request)


def delete(request):
    d=request.GET.get('del')
    CourseregModel.objects.filter(cid=d).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewall')

#StudentFunctions

def register(request):
    return render(request,"Sregister.html")

def sreg(request):
    un = request.POST.get("a1")
    a = request.POST.get("a2")
    b = request.POST.get("a3")
    c = request.POST.get("a4")
    d = request.POST.get("a5")
    StudentlogModel(uname=un,name=a, contactno=b, email=c, password=d).save()
    messages.success(request, 'registred successfully')
    return redirect('register')



def slogin(request):
    un = request.POST.get('a1')
    pa = request.POST.get('a2')
    try:
        sn = StudentlogModel.objects.get(uname=un, password=pa )
        return render(request, "Shome.html", {'name': sn})
    except StudentlogModel.DoesNotExist:
        return render(request, "Slogin.html", {"msg": 'Username or Password is incorrect'})



def shome(request):
    uname = request.GET.get("sn")
    return render(request,"Shome.html",{"name":uname})

def sView(request):

    data = CourseregModel.objects.all()
    return render(request, "Sview.html" , {"data":data})

def enroll(request):
    c = request.GET.get('no')
    i = request.GET.get('sid')

    #print(c,i)
    #studentCourse(cid=c,sid=i).save()
    #print('data save')
    #return render(request, 'Sview.html')
    try:
        sn=studentCourse.objects.get(sid=i,cid=c)
        messages.error(request, "Already Entrolled",{"data":sn})
        return render(request,"Sview.html")
    except studentCourse.DoesNotExist:
        studentCourse(sid=i, cid=c).save()
        messages.success(request, "Enrolled Successfully")
        return render(request,"Sview.html")


def venroll(request):
    sid = request.GET.get('sid')
    res = studentCourse.objects.filter(sid=sid)
    coures = [CourseregModel.objects.get(cid=x.cid) for x in res]
    return render(request, 'view_enroll.html', {'data': coures})


    #sid = request.GET.get('sid')
    #res = studentCourse.objects.filter(sid= sid)
    #course = [CourseregModel.objects.get(cid=id=x.cid) for x in res]
    #return render(request,"view_enroll.html",{"data":course})

def sdelete(request):
    cno = request.POST.get('cno')
    sid = request.POST.get('sid')
    studentCourse.objects.get(cid=cno,sid=sid).delete()
    res = studentCourse.objects.filter(sid=sid)
    data = [studentCourse.objects.get(cid=x.cid) for x in res]
    return render(request,"delete_course.html",{"data": data})

def student_logout(req):
    del req.session['sid']
    return redirect('slogin')


def contact(request):
    return render(request,"contact.html")


