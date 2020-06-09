from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def sucess(request):
    return render(request, "sucess.html")

def home_task(request):
    return render(request, "home_task.html")
# Create your views here.
def login_des(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("sucess")
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, "login_des.html")

    return render(request, "login_des.html")

def register_des(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken, Try a different user name...')
                return redirect("register_des")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken, Use a new email...')
                return redirect("register_des")
                
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'Account Created, Please Login')
                return redirect("login_des")

        else:
            messages.info(request,'Password Mismatch')
            return redirect("register_des")
        return redirect("login_des")
    return render(request, "register_des.html")

def logout_des(request):
    auth.logout(request)
    return redirect('/')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.info(request, 'Your password was successfully updated, Please login again....')
            return redirect('login_des')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_reset_form.html', {
        'form': form
    })