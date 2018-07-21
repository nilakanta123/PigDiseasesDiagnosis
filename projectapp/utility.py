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
	res['discharge']=[tuple(x) for x in s_list[81:89].values]
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

def diseases_predict_engine(ll):
	df = pd.read_csv('data/am.csv')
	# df.drop(['Probable_agent'], axis=1, inplace=True)	
	labelEncoder = preprocessing.LabelEncoder()
	if df['Probable_disease'].size > 0:
		labelEncoder.fit(df['Probable_disease'])
	df['Probable_disease']=labelEncoder.transform(df['Probable_disease'])
	X, y = shuffle(df.iloc[:,:-3],df.Probable_disease, random_state=13)
	model_svm = SVC(C=26, gamma=0.01, kernel='rbf', probability=True)
	model_svm.fit(X,y)
	pred = (-model_svm.predict_proba([ll])).argsort()[0]
	return labelEncoder.inverse_transform(pred[:3])


def decision_predict_engine(ll,st):
	df = pd.read_csv('data/am.csv')
	# df.drop(['Probable_agent'], axis=1, inplace=True)	
	pdle = preprocessing.LabelEncoder()
	pale = preprocessing.LabelEncoder()
	dle = preprocessing.LabelEncoder()
	if df['Probable_disease'].size > 0:
		pdle.fit(df['Probable_disease'])
	if df['Probable_agent'].size > 0:
		pale.fit(df['Probable_agent'])
	if df['Decision'].size > 0:
		dle.fit(df['Decision'])
	df['Probable_disease']=pdle.transform(df['Probable_disease'])
	df['Probable_agent']=pale.transform(df['Probable_agent'])
	df['Decision']=dle.transform(df['Decision'])
	X, y = shuffle(df.iloc[:,:-2],df.Decision, random_state=13)
	model2_svm = SVC(C=26, gamma=0.01, kernel='rbf', probability=True)
	model2_svm.fit(X,y)
	ss = pdle.transform([st])
	ll.extend(ss)
	pred = model2_svm.predict([ll])[0]
	return dle.inverse_transform(pred)

# l = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
# s = 'Screwworm flies infestation or Myiasis'
# ree = decision_predict_engine(l,s)
# print(ree)