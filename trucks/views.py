from django.shortcuts import render

# Create your views here.
def showtruck(request):
    trucks = request.GET['trucks']
    print (trucks)
    context = {
        'trucks':trucks,
    }
    return render(request,'truck.html',context=context)