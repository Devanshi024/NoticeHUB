from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authLogin,logout
import sys

# Create your views here.
def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')  
        email = request.POST.get('email')  
        pass1 = request.POST.get('password1')  
        pass2 = request.POST.get('password2')  

        if pass1 != pass2:
            return HttpResponse("Passwords are not same")
        else: 
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request,username=username,password = pass1)
        if user is not None:
            authLogin(request,user)
            return redirect('Notice')
        else:
            return HttpResponse("Username or password is invalid")
       
    return render(request,'login.html')



def logout(request):
    
    logout(request)
    return redirect('login')

