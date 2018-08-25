from django.shortcuts import render, redirect
from .forms import PageOneForm, PageTwoForm, FeedbackForm
from .utility import get_am_symptom_list,  get_pm_symptom_list, get_am_input, get_pm_input, am_diseases_predict_engine, am_decision_predict_engine, pm_diseases_predict_engine, pm_decision_predict_engine, mrange

def page_am(request):
	if request.method == 'POST':
		form = PageOneForm(request.POST)
		if form.is_valid():
			checked_list = request.POST.getlist('checks')
			if len(checked_list) > 0:
				user_input = get_am_input(checked_list)
				diseases, scores = am_diseases_predict_engine(user_input)
				decision = am_decision_predict_engine(user_input, diseases[0])
				request.session['decision'] =decision
				request.session['disease1'] =diseases[0]
				request.session['score1'] = int(scores[0])
				request.session['range1'] = mrange(int(scores[0]))
				request.session['disease2'] =diseases[1]
				request.session['score2'] = int(scores[1])
				request.session['range2'] = mrange(int(scores[1]))
				request.session['disease3'] =diseases[2]
				request.session['score3'] = int(scores[2])
				request.session['range3'] = mrange(int(scores[2]))
				return redirect('page_am_result')
				# return render(request, 'page_antimortem_result.html',{'finding': diseases,
				# 	'score1': int(scores[0]), 'range1': mrange(int(scores[0])),
				# 	'score2': int(scores[1]), 'range2': mrange(int(scores[1])),
				# 	'score3': int(scores[2]), 'range3': mrange(int(scores[2])),
				# 	'decision': decision})
	else:
		form = PageOneForm()
	dic = get_am_symptom_list()
	return render(request, 'page_antimortem.html', {"age":dic['age'],"general":dic['general'],"skin":dic['skin'],
				"breathing":dic['breathing'],"digestive":dic['digestive'],"behavioural":dic['behavioural'],
				"posture":dic['posture'],"structure":dic['structure'],"discharge":dic['discharge'],})


def page_pm(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PageTwoForm(request.POST)
		 # check whether it's valid:
		if form.is_valid():
			 # process the data in form.cleaned_data as required
			checked_list = request.POST.getlist('checks')
			if len(checked_list) > 0:
				user_input = get_pm_input(checked_list)
				diseases, scores = pm_diseases_predict_engine(user_input)
				decision = pm_decision_predict_engine(user_input,  diseases[0])
				request.session['decision'] =decision
				request.session['disease1'] =diseases[0]
				request.session['score1'] = int(scores[0])
				request.session['range1'] = mrange(int(scores[0]))
				request.session['disease2'] =diseases[1]
				request.session['score2'] = int(scores[1])
				request.session['range2'] = mrange(int(scores[1]))
				request.session['disease3'] =diseases[2]
				request.session['score3'] = int(scores[2])
				request.session['range3'] = mrange(int(scores[2]))
				# return render(request, 'page_postmortem_result.html',{'finding':diseases, 'decision': decision})
				return redirect('page_pm_result')
	 # if a GET (or any other method) we'll create a blank form
	else:
		form = PageTwoForm()

	dic = get_pm_symptom_list()
	return render(request, 'page_postmortem.html', {"sex":dic['sex'],"head":dic['head'],"skin":dic['skin'],
			"muscle":dic['muscle'],"pleura":dic['pleura'],"lymphnode":dic['lymphnode'],"udder":dic['udder'],
			"lung":dic['lung'],"heart":dic['heart'],"epligotis":dic['epligotis'],"stomach":dic['stomach'],
			"intestine":dic['intestine'],"liver":dic['liver'],"spleen":dic['spleen'],"gallbladder":dic['gallbladder'],
			"bileduct":dic['bileduct'],"pancreaticduct":dic['pancreaticduct'],"kidney":dic['kidney'],
			"urinarybladder":dic['urinarybladder'],"uterus":dic['uterus'],"testicles":dic['testicles'],"joinbone":dic['joinbone'],
			"abdominalcavity":dic['abdominalcavity'],"thorasiccavity":dic['thorasiccavity'],"specialcondition":dic['specialcondition'],
			"pmimethodvisual":dic['pmimethodvisual'],"condition":dic['condition'],})


def page_am_result(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FeedbackForm(request.POST)
		 # check whether it's valid:
		if form.is_valid():
			print("\n NOW WRITE CODE FOR SAVING FEEDBACK \n")
			return redirect('page_am')
	else:
		form = FeedbackForm()

	return render(request, 'page_antimortem_result.html',
		{'decision':request.session.get('decision'),
		'disease1':request.session.get('disease1'),
		'disease2':request.session.get('disease2'),
		'disease3':request.session.get('disease3'),
		'score1':request.session.get('score1'),
		'score2':request.session.get('score2'),
		'score3':request.session.get('score3'),
		'range1':request.session.get('range1'),
		'range2':request.session.get('range2'),
		'range3':request.session.get('range3'),})

def page_pm_result(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FeedbackForm(request.POST)
		 # check whether it's valid:
		if form.is_valid():
			print("\n NOW WRITE CODE FOR SAVING FEEDBACK \n")
			return redirect('page_pm')
	else:
		form = FeedbackForm()

	return render(request, 'page_postmortem_result.html',
		{'decision':request.session.get('decision'),
		'disease1':request.session.get('disease1'),
		'disease2':request.session.get('disease2'),
		'disease3':request.session.get('disease3'),
		'score1':request.session.get('score1'),
		'score2':request.session.get('score2'),
		'score3':request.session.get('score3'),
		'range1':request.session.get('range1'),
		'range2':request.session.get('range2'),
		'range3':request.session.get('range3'),})

