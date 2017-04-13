from django.conf.urls import url
from django.shortcuts import render

from django.views import generic
from .models import Champ
from . import views
from django.http import HttpResponse

# def index(request):
# 	return HttpResponse("<h1> YOU ARE IN INDEX DE CHAMPIGNONS !!! </h1>")

def route(request):
	return render(request, 'home/heroic.html')

def sliderz(request):
	return render(request, 'home/sliderz.html')

def levures(request):
	return render(request, 'home/jumbox.html')


class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'ma_liste'
	def get_queryset(self):
		return Champ.objects.all()

class DetailView(generic.DetailView):
	model = Champ
	template_name = 'home/detail.html'


