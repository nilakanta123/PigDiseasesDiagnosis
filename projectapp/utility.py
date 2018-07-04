import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn.svm import SVC

def get_separated_symptom_list():
	res = {}
	s_list = pd.read_csv("data/info.csv")
	res['age']=[tuple(x) for x in s_list[0:6].values]
	res['general']=[tuple(x) for x in s_list[6:18].values]
	res['skin']=[tuple(x) for x in s_list[18:38].values]
	res['breathing']=[tuple(x) for x in s_list[38:46].values]
	res['digestive']=[tuple(x) for x in s_list[46:53].values]
	res['behavioural']=[tuple(x) for x in s_list[53:66].values]
	res['posture']=[tuple(x) for x in s_list[66:75].values]
	res['structure']=[tuple(x) for x in s_list[75:81].values]
	res['discharge']=[tuple(x) for x in s_list[81:].values]
	return res

def get_user_input(ll):
	s_list = pd.read_csv("data/info.csv")
	res = []
	for i in s_list['symptoms']:
		if i in ll:
			res.append(1)
		else:
			res.append(0)
	return res

def predict_engine(ll):
	df = pd.read_csv('data/am.csv')
	df.drop(['Probable_agent'], axis=1, inplace=True)	
	labelEncoder = preprocessing.LabelEncoder()
	if df['Probable_disease'].size > 0:
		labelEncoder.fit(df['Probable_disease'])
	df['Probable_disease']=labelEncoder.transform(df['Probable_disease'])
	X, y = shuffle(df.iloc[:,:-1],df.Probable_disease, random_state=13)
	model_svm = SVC(C=26, gamma=0.01, kernel='rbf')
	model_svm.fit(X,y)
	return labelEncoder.inverse_transform(model_svm.predict([ll]))

