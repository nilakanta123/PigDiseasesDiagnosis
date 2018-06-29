from django.shortcuts import render

def page_one(request):
	return render(request, 'pageone.html',{})
