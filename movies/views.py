from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from movies.models import movies
from movies.forms import movieform
from movies.serializers import movie_serializer
from rest_framework.views import APIView
from rest_framework.response import Response


class home(ListView):
    model=movies
    template_name='movie_home.html'
    context_object_name='movie'

class add_movie(View):
    def get(self, request):
        form=movieform
        return render(request, 'add_movie.html', { 'form':form })

    def post(self, request):
        data_form=movieform(request.POST)
        if data_form.is_valid():
            data_form.save()
            return redirect('add')

class apiview(APIView):
    def get(self, request):
        data=movies.objects.all()
        serial=movie_serializer(data, many=True)
        return Response(serial.data)