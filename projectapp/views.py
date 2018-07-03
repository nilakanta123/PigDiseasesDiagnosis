from django.shortcuts import render
from .forms import PageOneForm
from .utility import get_separated_symptom_list, get_symptom_list

def page_one(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PageOneForm(request.POST)
		 # check whether it's valid:
		if form.is_valid():
			 # process the data in form.cleaned_data as required
			print(request.POST.getlist('checks'))
			print("and")
			print(get_symptom_list())
			print("\nWORKING TILL HERE\n")
			 # redirect to a new URL:
			return render(request, 'pagetwo.html',{})
	 # if a GET (or any other method) we'll create a blank form
	else:
		form = PageOneForm()


	dic = get_separated_symptom_list()
	return render(request, 'pageone.html', {"age":dic['age'],"general":dic['general'],"skin":dic['skin'],
				"breathing":dic['breathing'],"digestive":dic['digestive'],"behavioural":dic['behavioural'],
				"posture":dic['posture'],"structure":dic['structure'],"discharge":dic['discharge'],})