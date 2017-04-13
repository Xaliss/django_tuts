from django.shortcuts import render, redirect
from django.conf.urls import url
from django.views import generic
from .models import Livre
from . import views
from django.http import HttpResponse
from django.views.generic import ListView


def kilikili(request):
	return HttpResponse("<h1> YOU ARE IN KILI KILI !!!</h1>")

def kalakala(request):
	return HttpResponse("<h1> YOU ARE IN KALA KALA !!! </h1>")	

def home(request):
	return render(request, 'home/homz.html')	

def blog(request):
	return render(request, 'home/blog.html')

def route(request):
	return HttpResponse("<h1> EN ROUTE !!! </h1>")


class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'ma_liste'
	def get_queryset(self):
		return Livre.objects.all()

class DetailView(generic.DetailView):
	model = Livre
	template_name = 'home/detail.html'

class IxeView(generic.DetailView):
	# model = Livre
	template_name = 'home/detailx.html'
	queryset = Livre.objects.all()

def create(request):
	print (request.POST)
	livre = Livre(titre=request.POST['titre'], resume=request.POST['resume'])
	livre.save()
	return redirect('/webmike')

def edit(request,id):
	livre= Livre.objects.get(id=id)
	context = {"livre":livre}
	return render(request, 'home/edit.html', context)

def update(request,id):
	livre = Livre.objects.get(id=id)
	livre.titre  = request.POST['titre']
	livre.resume = request.POST['resume']
	livre.save()
	return redirect('/webmike')

def efface(request,id):
	
	livre = Livre.objects.get(id=id)
	livre.delete()
	return redirect('/webmike')