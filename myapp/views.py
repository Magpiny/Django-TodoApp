from django.shortcuts import render, get_object_or_404

from .models import TodoForm
from django.http import HttpResponseRedirect
from .forms import MyForm

# Create your views here.
def home(request):
    todos = TodoForm.objects.all()
    return render(request, 'myapp/home.html', {'todos':todos})

def index(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
    else:
        form = MyForm()
    
    
    return render(request, 'myapp/index.html', {'form':form})


def edit(request, pk=None):
    todo = get_object_or_404(TodoForm, pk=pk)
    if request.method == "POST":
       form = MyForm(request.POST, instance=todo)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect("/")
    else:
        form = MyForm(instance=todo)

    return render(request, 'myapp/edit.html', {'form':form})


def delete(request, pk=None):
    todo = get_object_or_404(TodoForm, pk=pk)
    todo.delete()

    return render(request, 'myapp/delete.html')
