# views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm,TodoListForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'content/register.html', {'form': form})


def todolistform(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = TodoListForm()
    return render(request, 'content/todolistform.html', {'form': form})