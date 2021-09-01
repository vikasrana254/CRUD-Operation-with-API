from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import  StudentRegistration
from .models import User
# This function use for Add and Show data
def showdata(request):
    if request.method=="POST":
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg= User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration
    else:
        fm = StudentRegistration
    stud= User.objects.all()
    return render(request, 'course/addshow.html', {'form':fm,
           'stu':stud})

# This function use for delete
def delete_data(request, id):
    if request.method == "POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# This function use for edit
def update(request, id):
     if request.method == "POST":
        pi=User.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
           fm.save()
     else:
        pi=User.objects.get(pk=id)
        fm= StudentRegistration(instance=pi)
        return render(request, 'course/update.html', {'form':fm})

