# i have created this file - Vaibhav
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def analyze(request):
	# Get the text
	djtext = request.POST.get('text', 'default')

	# check checkbox value
	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')
	extraspaceremover = request.POST.get('extraspaceremover', 'off')

	analyzed = ""

	# check which checkbox is on
	if removepunc == 'on':
		punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
		# Analyse the text
		return render(request, 'analyze.html', params)
	
	elif fullcaps == 'on':
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {'purpose':'Changed to UPPERCASE', 'analyzed_text':analyzed}
		# Analyse the text
		return render(request, 'analyze.html', params)

	elif newlineremover == 'on':
		for char in djtext:
			if char != '\n' and char != '\r':
				analyzed = analyzed + char
		params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
		# Analyse the text
		return render(request, 'analyze.html', params)

	elif extraspaceremover == 'on':
		for index, char in enumerate(djtext):
			if not (djtext[index] ==' ' and djtext[index+1] == ' '):
				analyzed = analyzed + char
		params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
		# Analyse the text
		return render(request, 'analyze.html', params)

	else:
		return HttpResponse('Error')
