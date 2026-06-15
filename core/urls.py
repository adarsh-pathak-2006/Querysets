from django.contrib import admin
from django.urls import path
from .views import home, Login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('home/', home.as_view(), name='home'),
    path('register/', register.as_view(), name='register'),
]