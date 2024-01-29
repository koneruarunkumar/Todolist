from django.shortcuts import render,redirect
from datetime import datetime
from .models import TodoListData
from datetime import datetime



def index(request):
    current_time=datetime.now()
    if request.method =='GET':
        data=TodoListData.objects.all()
        return render(request,'indexpage.html',{'data':data})

    else:
        TodoListData(
        title=request.POST.get('title'),
        details=request.POST.get('details'),
        current_time = datetime.now()
        ).save()

        data=TodoListData.objects.all()
        return render(request,'indexpage.html',{'data':data})

def delete_data(request,id):
    data=TodoListData.objects.get(id=id)
    data.delete()
    return redirect('index')

def update(request,id):
    row=TodoListData.objects.get(id=id)
    return render(request,'update.html',{'row':row})


def updateddata(request,id):
    data=TodoListData.objects.get(id=id)
    data.title=request.POST.get('title')
    data.details=request.POST.get('details')
    data.save()
    return redirect('index')
