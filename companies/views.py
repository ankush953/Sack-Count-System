from django.shortcuts import render, redirect
from companies.forms import CompanyRegistrationForm
from django.contrib import messages

# Create your views here.
def company_registration(request):
    registrationform = CompanyRegistrationForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if registrationform.is_valid():
            registrationform.save()
            messages.success(request,"Congrats! Company is registered.")
            return redirect('home')
    context = {
        'form':registrationform,
    }
    return render(request,'companyregister.html',context=context)
            