from django.shortcuts import render
from .utility import get_symptom_list

def page_one(request):
	dic = get_symptom_list()
	return render(request, 'pageone.html',{"age":dic['age'],"general":dic['general'],"skin":dic['skin'],
		"breathing":dic['breathing'],"digestive":dic['digestive'],"behavioural":dic['behavioural'],
		"posture":dic['posture'],"structure":dic['structure'],"discharge":dic['discharge'],})
