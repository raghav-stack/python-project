from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm


def todos(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('todos')
    else:
        form = TodoForm()

    todos = Todo.objects.filter(is_done=False)

    return render(request, 'todos.html', {'todos': todos, 'form': form})

def todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    change_status = request.GET.get('change_status', '')

    if change_status:
        todo.is_done = True
        todo.save()

    return render(request, 'todo.html', {'todo': todo})

