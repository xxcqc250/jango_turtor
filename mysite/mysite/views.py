from django.http import HttpResponse
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response

def here(request):
	return HttpResponse('everyone im here')

def math(request):
	s=5
	d=3
	p=1
	q=0
	# with open('templates/math.html','r') as reader:
	# 	t = template.Template(reader.read())
	# t=get_template('math.html')
	# c = template.Context({'s':s,'d':d,'p':p,'q':q})
	# return HttpResponse(t.render(c))	
	# return render_to_response('math.html',{'s':s,'d':d,'p':p,'q':q})
	return render_to_response('math.html',locals())