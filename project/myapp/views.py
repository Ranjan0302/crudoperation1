from django.shortcuts import render,redirect
from .forms import*

# Create your views here.


def user(request):
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url_name')
        else:
            form=UserForm()
        return render(request,'User.html',{'form':form})   


def tasks(request):
    if request.method =='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return ('task_added_successfully')
        else:
            form=TaskForm()
        return render(request,'Task.html',{'form':form})   
