from django.shortcuts import render, redirect
from .models import User_list, Attendance
# from django.core.mail import EmailMessage
# from django.contrib.auth import hashers
# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy
def createuser(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        date_of_join = request.POST['date_of_join']
        superuser = request.POST['superuser']
        song=User_list()
        song.first_name=first_name
        song.last_name=last_name
        song.password=password
        song.email=email
        song.date_of_join=date_of_join
        if superuser=='Admin':
            song.superuser=True
        else:
            pass
        song.save()
        return redirect('index')
    else:
        return render(request, 'Account/userlist_form.html', {'errror': 5})

def add_attendance(request,id):
    user = User_list.objects.get(pk=id)
    if request.method=='POST':
        song=Attendance()
        date=request.POST['date']
        status=request.POST['status']
        if(status=='Present'):
            song.status=True
        else:
            pass
        song.date=date
        song.user=user
        song.save()
        #email = EmailMessage('Attendance Update', 'Check Your Updated attendance', to=[user.email])
        #email.send()
        return redirect('admin_attendance',user.id)
    else:
        return render(request, 'Account/create_attendance.html', {'errror': 5,'data':user})

def login(request):
    #errror=hashers.make_password('hellodj21')
    if (request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        useer=User_list.objects.all()
        x=0
        for detail in useer:
            if (email==detail.email)and(password==detail.password):
                x=1
                z=detail.id
            else:
                pass
        if (x==1):
            user = User_list.objects.get(pk=z)
            if(user.superuser):
                return redirect('index')
            else:
                return redirect('staff_login',z)

        else:
            error='Invalid Credentials'
            return render(request,'Account/login.html',{'error':error})
    else:
        return render(request,'Account/login.html',{'errorr':5})
def index(request):
    data=User_list.objects.all()
    return render(request,'Account/index.html',{'data':data})
def staff_login(request,id):
    user=User_list.objects.get(pk=id)
    if request.method=="POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        list1=[]

        list3=[]
        for song in user.attendance_set.all():
            a=song.date
            if (a>=date1)and(a<=date2):
                list3.append(song.date)
                list3.append(song.id)
                list3.append(song.status)
                list1.append(list3)
                list3 = []
        return render(request,'Account/sorted_staff_attendance.html',{'data':user,'list1':list1})
    else:
        return render(request,'Account/attendance_staff_detail.html',{'data':user})
def admin_user_attendance(request,id):
    user=User_list.objects.get(pk=id)
    if request.method=="POST":
        date1=request.POST['date1']
        date2=request.POST['date2']
        list1=[]
        list3=[]
        for song in user.attendance_set.all():
            a=song.date
            if (a>=date1)and(a<=date2):
                list3.append(song.date)
                list3.append(song.id)
                list3.append(song.status)
                list1.append(list3)
                list3 = []
        return render(request,'Account/sorted_attendance.html',{'data':user,'list1':list1})
    else:
        return render(request,'Account/attendance_detail.html',{'data':user})
def update_user(request,id):
    user=User_list.objects.get(pk=id)
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        date_of_join = request.POST['date_of_join']
        superuser = request.POST['superuser']

        user.first_name = first_name
        user.last_name = last_name
        user.password = password
        user.email = email
        user.date_of_join = date_of_join
        if superuser == 'Admin':
            user.superuser = True
        else:
            user.superuser = False
        user.save()
        return redirect('index')
    else:
        return render(request,'Account/update_user.html',{'data':user})
def update_attendance(request,id,value):
    user=Attendance.objects.get(pk=id)
    data=User_list.objects.get(pk=value)
    if request.method=='POST':
        date=request.POST['date']
        status=request.POST['status']

        if(status=='Present'):
            user.status=True
        else:
            user.status=False
        user.date=date
        user.save()
        #email = EmailMessage('Attendance Update', 'Your attendance has been updated', to=[data.email])
        #email.send()
        return redirect('admin_attendance',data.id)
    else:
        return render(request, 'Account/update_attendance.html', {'data':data,'user':user})
def delete_user(request,id):
    data = User_list.objects.get(pk=id)
    if request.method=='POST':
        User_list.objects.filter(pk=id).delete()
        return redirect('index')
    else:
        return render(request, 'Account/delete_user.html', {'data':data})
def delete_attendance(request,id,value):
    user = Attendance.objects.get(pk=id)
    data = User_list.objects.get(pk=value)
    if request.method=='POST':
        Attendance.objects.filter(pk=id).delete()
        return redirect('admin_attendance',data.id)
    else:
        return render(request, 'Account/delete_attendance.html', {'data':data,'user':user})
