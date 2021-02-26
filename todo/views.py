from todo.models import Todo
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    todo= Todo.objects.all()
    if request.method == 'POST':
        new_todo=Todo(
            title= request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request,'home.html',{'todolist':todo})

def delete(request,pk):
    todo= Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')