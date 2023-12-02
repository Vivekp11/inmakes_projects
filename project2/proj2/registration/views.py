from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, {'msg': messages})
#             return redirect('login.html')
#
#     return render(request, 'login.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('signin')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('signin')

            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                print("user created")
                # return redirect('log')
        else:
            messages.info(request, "password mismatch")
            return redirect('signin')
        return redirect('log')
    return render(request, 'register.html')

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('log')

    return render(request, 'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
