from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def signin(request):
    if request.method == "GET":
        return render(request, 'Sign_in/signin.html');
    else:
        username = request.POST.get('username')
        passwd = request.POST.get('password')
       
        check_all = authenticate(username=username, password=passwd)

        is_auth = False

        if check_all:
            return render(request, 'Home/home.html');
            
        else:
            is_auth = True

            return render(request, 'Sign_in/signin.html', {'is_auth': is_auth});

def signup(request):  
    if request.method == "GET":
        return render(request, 'Sign_up/signup.html');

    else:
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.filter(username=username).first()

        is_auth = False

        if user:
            is_auth = True

            return render(request, 'Sign_up/signup.html', {'is_auth': is_auth});
        

        new_user = User.objects.create_user(username=username, email=email, password=passwd)
        new_user.save()

        return render(request, 'Sign_up/confirm.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'Home/home.html');

    return render(request, 'Sign_in/signin.html'); 