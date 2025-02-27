from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from my_app.models import *


def index(request):
    return render(request,"home.html")



def login(request):
    return render(request,"login.html")

def login_post(request):
    username=request.POST['username']
    password=request.POST['pass']
    a=Login.objects.get(username=username,password=password)
    request.session['lid']=a.id

    if a.type=='admin':
        return HttpResponse('''<script>alert('Admin logined...');window.location='/admin_dash'</script>''')
    elif a.type=='user':
        return HttpResponse('''<script>alert('User logined...');window.location='/user_dash'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid...');window.location='/'</script>''')

def logout(request):
    request.session['lid']=''
    return redirect('/')


def admin_dash(request):
    if request.session['lid']=='':
        return redirect('/')
    return render(request,"Admin/Admin_dashboard.html")

def user_dash(request):
    if request.session['lid'] =='':
        return redirect('/')
    return render(request,"User/User_dashboard.html")

def registration(request):
    return render(request,"registration.html")



def registration_POST(request):
    name=request.POST['textfield4']
    email=request.POST['textfield3']
    phone=request.POST['textfield1']
    place=request.POST['textfield2']
    password=request.POST['pass1']
    confirmpassword=request.POST['pass2']
    if password == confirmpassword:
        lobj=Login()
        lobj.username=email
        lobj.password=password
        lobj.type="user"
        lobj.save()
        uobj=User()
        uobj.login_id=lobj
        uobj.name=name
        uobj.email = email
        uobj.place = place
        uobj.phone=phone
        uobj.save()
        return HttpResponse('''<script>alert('Account  successfully created...');window.location='/login'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid...');window.location='/registration'</script>''')
def view_feedback(request):
    if request.session['lid'] =='':
        return redirect('/')
    a=Feedback.objects.all()
    return render(request,"Admin/admin_view_feedback.html",{'data':a})

def view_user(request):
    if request.session['lid'] =='':
        return redirect('/')
    b=User.objects.all()
    return render(request,"Admin/admin_view_users.html",{'data':b})


def send_feedback(request):
    if request.session['lid'] =='':
        return redirect('/')

    return render(request,"User/send_feedback.html")


def send_feedback_post(request):
    feedback=request.POST['name']
    a=Feedback()
    a.user_id=User.objects.get(login_id_id=request.session['lid'])
    a.feedback=feedback
    a.save()
    return redirect('/user_dash')

def upload_image(request):
    if request.session['lid'] =='':
        return redirect('/')
    return render(request,"User/upload_image.html")