from django.urls import path
from .views import *


urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('home/', home.as_view(), name='home'),
    path('register/', register.as_view(), name='register'),
]