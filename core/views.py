from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView
from django.views import View
from .models import db
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


class home(View):
    def get(self, request):
        items=db.objects.all().order_by('age')
        return render(request, 'home.html', { 'items': items })
    
    def post(self, request):
        db.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender')
        )
        return redirect('home')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('pass')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return redirect('register')      

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
                User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('pass1')
                    )
                return redirect('home')
        else:
            return render(request, 'register.html', { 'pass_error': 'enter the same passwords in both fields' })
        
        
        

