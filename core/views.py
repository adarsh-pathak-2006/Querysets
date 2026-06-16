from django.shortcuts import render,redirect
from django.views import View
from .models import db
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        user=authenticate(request, username=request.POST.get('username'),
                          password=request.POST.get('password'))
        
        if user is not None:
            login(request, user)
            return redirect('home')

class register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                return redirect('login')
            else:
                user=User.objects.create_user(username=username, password=pass1)
                login(request, user)
                return redirect('home')
        
        else:
            return render(request, 'register.html', { 'pass_err':'enter the same password in both fields' })

class home(View):
    def get(self, request):
        data=db.objects.all()
        return render(request, 'home.html', { 'data':data })
    
    def post(self, request):
        db.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            user=request.user,
        )
        return redirect('home')




