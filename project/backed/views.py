from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
# Create your views here.

def index(request):
    
    return render(request, 'index.html')



def login(request):
    ctx = {}
    if request.method != 'POST':
        return render(request, 'login.html', ctx)

    ctx['name'] = name = request.POST.get('name', '')
    ctx['password'] = password = request.POST.get('password', '')
    ctx['errors'] = errors = []
    user = User.objects.filter(name=name, password=password, status=0).first()
    if not user:
        errors.append('用户名和密码错误!')
        return render(request, 'login.html', ctx)

    return redirect('index')


@csrf_exempt
def register(request):
    ctx = {}
    ctx['name'] = name = request.POST.get('name', '')
    ctx['password'] = password = request.POST.get('password', '')
    ctx['errors'] = errors = []
    action = request.POST.get('action', '')
    if action == 'add_user':
        user = User.objects.filter(name=name, status=0).first()
        if user:
            errors.append('用户名已存在')
            return render(request, 'register.html', ctx)
        else:
            User.objects.create(name=name, password=password)
            return redirect('login')

    return render(request, 'register.html', ctx)

@csrf_exempt
def index2(request):
    
    return render(request, 'index2.html')

    