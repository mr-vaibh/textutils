# i have created this file - Vaibhav
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def removepunc(request):
	djtext = request.GET.get('text', 'default')
	return HttpResponse('remove punctuations')

def newlineremove(request):
	return HttpResponse('new line remove')

def capfirst(request):
	return HttpResponse('capitalize first')

def spaceremover(request):
	return HttpResponse('space remover')

def charcount(request):
	return HttpResponse('character count')


def about(request):
	return HttpResponse("About to launch ;)")