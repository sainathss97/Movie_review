from cmath import log
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password= request.POST['password1']
                 )
                user.save()
                print("User Saved!!")
                login(request,user)
                print("login Success!!")
                return redirect('home')
            except IntegrityError:
                return render(request,'signupaccount.html',
                              {'form': UserCreateForm,
                 'error': 'Username is already taken'
                })
        else:
            print("Passwords dont match!!")
            return render(request, 'signupaccount.html', {'form': UserCreateForm,
                                                            'error':'Passwords are not matching'})


@login_required
def logoutaccount(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm,
                                                        'error':'😎 A Fine Day When you are Around 😎'})
    else:
        user = authenticate(request,username = request.POST['username'],
                                    password = request.POST['password'])
        if user is None:                            
            return render(request,'loginaccount.html',{'form': AuthenticationForm,
                                                        'error':'Username and Password Doesnot match 🥲'})
        else:
            login(request,user)
            return redirect('home')