# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from ConvertToText import convertPDFToText, convertDocxToText
from parser import getEmail, getPhone, getName
from django.views.decorators.csrf import csrf_exempt

from .models import parsedResume
from django.contrib import messages


# Create your views here.

def convertToText(path):
    import textract
    # path= os.path.join(settings.BASE_DIR, path)
    # path = os.path.abspath(path)
    # print(path)
    text = textract.process(path)
    return text

def dashboard(request):
	context = {}
	return render(request, 'core/dashboard.html', context)

def parsed(request):
	parsed = parsedResume.objects.all()
	context = {
		'parsed': parsed,
	}
	return render(request, 'core/parsed.html', context)

@csrf_exempt
def parse(request):
	if request.method == "POST":
		print(request.POST)
		file = request.FILES['resume'] #POST.get('resume')
		temp = parsedResume(file = file)
		temp.save()

		print(temp.file.path)

		text = convertToText(temp.file.path)

		name = getName(text)
		email = getEmail(text)
		phone = getPhone(text)

		print(email)

		temp.name = name
		temp.email = email
		temp.phone = phone

		temp.save()

		context = {
			'data': temp,
		}
		# messages.add_message(request, messages.INFO, ';hello')


		# return redirect('dashboard')
		return render(request, 'core/dashboard.html', context)
