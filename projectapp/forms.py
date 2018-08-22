from django import forms
from django.apps import apps
# from .utility import get_other_symptoms


class PageOneForm(forms.Form):
	
	# myset =[]
	# for i in get_other_symptoms():
	# 	myset.append((i,i))
	# other_symptoms = forms.CharField(required=False, widget=forms.SelectMultiple(choices=myset))

	def __init__(self, *args, **kwargs):
		super(PageOneForm, self).__init__(*args, **kwargs)

class PageTwoForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(PageTwoForm, self).__init__(*args, **kwargs)