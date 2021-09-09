from django.shortcuts import render,redirect
from .forms import CreatUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreatUserForm()
        if request.method == 'POST':
            form = CreatUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User ' + '' + user + '' + ' have been created now you can login')
                return redirect('login')
    context = {'form':form}
    return render(request, 'registration/signup.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Password or username are incorrect')
    context = {}
    return render(request, 'registration/login.html', context)



def logout_user(request):
    logout(request)
    return redirect('login')
