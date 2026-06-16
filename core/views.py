from django.shortcuts import render,redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import db
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .serializer import db_serializer
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        user=authenticate(request, username=request.POST.get('username'),
                          password=request.POST.get('password'))
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')

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

class home(LoginRequiredMixin, View):
    def get(self, request):
        data=db.objects.filter(user=request.user)
        return render(request, 'home.html', { 'data':data })
    
    def post(self, request):
        db.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            user=request.user,
        )
        return redirect('home')

class apiView(LoginRequiredMixin, APIView):
    def get(self, request):
        data=db.objects.filter(user=request.user)
        serialized=db_serializer(data, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized=db_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return redirect('apiview')
        else:
            print('Hail Hitler')


class individual(APIView):
    def get(self, request, id):
        data=db.objects.filter(user=request.user).get(id=id)
        serialized=db_serializer(data)
        return Response(serialized.data)
    
