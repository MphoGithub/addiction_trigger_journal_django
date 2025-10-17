from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully! You can now log in')
            return redirect('home')
        
    else:
        form = UserRegistrationForm()
            
    context = {'form':form}
    return render(request,'users/register.html',context)
        