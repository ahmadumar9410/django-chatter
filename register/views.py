from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('User Already Taken')
            elif User.objects.filter(email=email).exists():
                print('Email Already Taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=fullname)
                user.save()
                print('User Created')
                return redirect('/')
    else:
        pass
    return render(request, 'sign-up.html')
