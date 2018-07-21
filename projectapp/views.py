from django.shortcuts import render
from .forms import PageOneForm
from .utility import get_separated_symptom_list, get_user_input, diseases_predict_engine, decision_predict_engine

def page_one(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PageOneForm(request.POST)
		 # check whether it's valid:
		if form.is_valid():
			 # process the data in form.cleaned_data as required
			checked_list = request.POST.getlist('checks')
			if len(checked_list) > 0:
				user_input = get_user_input(checked_list)
				diseases = diseases_predict_engine(user_input)
				decision = decision_predict_engine(user_input, diseases[0])
				return render(request, 'pagetwo.html',{'finding': diseases, 'decision': decision})
	 # if a GET (or any other method) we'll create a blank form
	else:
		form = PageOneForm()

	dic = get_separated_symptom_list()
	return render(request, 'pageone.html', {"age":dic['age'],"general":dic['general'],"skin":dic['skin'],
				"breathing":dic['breathing'],"digestive":dic['digestive'],"behavioural":dic['behavioural'],
				"posture":dic['posture'],"structure":dic['structure'],"discharge":dic['discharge'],})