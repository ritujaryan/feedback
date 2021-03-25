from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Analytics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Analytics
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.method == "GET": 
        return render(request, 'home.html')
    else:
        nam = request.POST.get('username')
        comp = request.POST.get('Competency')
        tea = request.POST.get('TeachingSkills')
        pun = request.POST.get('Punctuality')
        pra = request.POST.get('PracticalKnowledge')
        appr = request.POST.get('Approachability')
        control = request.POST.get('ClassControl')
        obj = Analytics( name= nam, competen = comp,teach = tea,punc = pun,prac=pra,approach = appr,classcontrol = control)
        obj.save()
        # print(nam,comp,tea,pun,pra,appr,control)
        messages.success(request, 'Feedback submission successful')
        return render(request, 'home.html')     

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('https://ra-feedback.herokuapp.com/analytics')
            return redirect('https://ra-feedback.herokuapp.com/home')

        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login1.html')

@login_required
def analytics(request):
    rows = Analytics.objects.all()
    user = request.user
    print(user)
    if user.is_staff:
        return render(request, 'analytics.html', {'data': rows})
    else:
        messages.info(request, 'Only teachers can access this page')
    return redirect('https://ra-feedback.herokuapp.com/login')
    # return render(request, 'login1.html')
