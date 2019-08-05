from django.shortcuts import render, redirect
from companies.forms import CompanyRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def company_registration(request):
    registrationform = CompanyRegistrationForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if registrationform.is_valid():
            registrationform.save()
            messages.success(request,"Congrats! Company is registered.")
            return redirect('home')
    isadmin = request.user.is_superuser
    context = {
        'form':registrationform,
        'title':'Register Company',
        'admin':request.user.is_superuser,
        'admin':isadmin,
    }
    return render(request,'companyregister.html',context=context)
            