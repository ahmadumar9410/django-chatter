from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            print('User Logged in succesfully')
            return redirect('/dashboard')
        else:
            print('Invalid Credentials')
    return render(request, 'sign-in.html')

def logout(request):
    auth.logout(request)
    return redirect('/')