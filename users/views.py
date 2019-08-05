from django.shortcuts import render, redirect, HttpResponseRedirect
from . import forms
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def new_user(request):
    newuserform = forms.NewUserForm(
        request.POST or None, request.FILES or None)
    basicform = forms.BasicForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if basicform.is_valid() and newuserform.is_valid():
            # print("here")
            moreinfo = newuserform.save(commit=False)
            basicinfo = basicform.save(commit=False)
            basicinfo.first_name = moreinfo.First_name
            basicinfo.last_name = moreinfo.Last_name
            basicinfo.email = moreinfo.Email_address
            basicinfo.set_password(basicinfo.password)

            if 'profile_pic' in request.FILES:
                moreinfo.profile_pic = request.FILES['profile_pic']
            else:
                moreinfo.profile_pic = 'profile_pic/default-user.jpg'
            basicinfo.save()
            moreinfo.user = basicinfo
            moreinfo.save()
            messages.success(request, "account created successfully.")
            return redirect('login')

    context = {
        'profileform': newuserform,
        'basicform': basicform,
        'title': 'Signup',
    }
    return render(request, 'signup.html', context=context)


def login_view(request):
    loginform = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('home')
    context = {
        'form': loginform,
    }

    return render(request, 'login.html', context=context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request,"You have been loggged out.")
    return redirect('home')


@login_required(login_url='login')
def update_profile(request, username):
    # if request.method == "POST":
    if request.user.username == username:
        user = User.objects.filter(username=username)[0]
        updateform = forms.UpdateForm(
            request.POST or None, request.FILES or None, instance=user)
        if request.method == "POST":
            if updateform.is_valid():
                pass
    messages.error(request, "Invalid access")
    return redirect('home')

@login_required(login_url='login')
def view_profile(request,username=None):
	user = User.objects.filter(username=username)[0]
	context = {
		'user':user,
	}
	return render(request,'profile.html',context=context)