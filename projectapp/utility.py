import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn.svm import SVC

def adjusting(sc):
	d = sc[0]-sc[1]
	if d < 5:
		dd = sc[1]-5
		sc[0] = sc[0]-dd
		sc[1] = sc[1]-dd
		sc[2] = sc[2]-dd

	if sc[2] < 0:
		sc[0] = sc[0]+ -(sc[2])
		sc[1] = sc[1]+ -(sc[2])
		sc[2] = sc[2]+ -(sc[2])

	return sc

def mrange(n):
	l = []
	for i in range(n):
		l.append(1)
	for j in range(10-n):
		l.append(0)
	return l

def get_am_symptom_list():
	res = {}
	s_list = pd.read_csv("./data/am_info.csv")
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

def get_pm_symptom_list():
	res = {}
	s_list = pd.read_csv("./data/pm_info.csv")
	res['sex']=[tuple(x) for x in s_list[0:2].values]
	res['head']=[tuple(x) for x in s_list[2:13].values]
	res['skin']=[tuple(x) for x in s_list[13:17].values]
	res['muscle']=[tuple(x) for x in s_list[17:20].values]
	res['pleura']=[tuple(x) for x in s_list[20:27].values]
	res['lymphnode']=[tuple(x) for x in s_list[27:32].values]
	res['udder']=[tuple(x) for x in s_list[32:33].values]
	res['lung']=[tuple(x) for x in s_list[33:49].values]
	res['heart']=[tuple(x) for x in s_list[49:57].values]
	res['epligotis']=[tuple(x) for x in s_list[57:58].values]
	res['stomach']=[tuple(x) for x in s_list[58:62].values]
	res['intestine']=[tuple(x) for x in s_list[62:73].values]
	res['liver']=[tuple(x) for x in s_list[73:82].values]
	res['spleen']=[tuple(x) for x in s_list[82:88].values]
	res['gallbladder']=[tuple(x) for x in s_list[88:90].values]
	res['bileduct']=[tuple(x) for x in s_list[90:93].values]
	res['pancreaticduct']=[tuple(x) for x in s_list[93:96].values]
	res['kidney']=[tuple(x) for x in s_list[96:105].values]
	res['urinarybladder']=[tuple(x) for x in s_list[105:107].values]
	res['uterus']=[tuple(x) for x in s_list[107:110].values]
	res['testicles']=[tuple(x) for x in s_list[110:115].values]
	res['joinbone']=[tuple(x) for x in s_list[115:121].values]
	res['abdominalcavity']=[tuple(x) for x in s_list[121:126].values]
	res['thorasiccavity']=[tuple(x) for x in s_list[126:130].values]
	res['specialcondition']=[tuple(x) for x in s_list[130:131].values]
	res['pmimethodvisual']=[tuple(x) for x in s_list[131:132].values]
	res['condition']=[tuple(x) for x in s_list[132:134].values]
	return res

def get_am_input(ll):
	s_list = pd.read_csv("./data/am_info.csv")
	res = []
	for i in s_list['symptoms']:
		if i in ll:
			res.append(1)
		else:
			res.append(0)
	return res



def get_pm_input(ll):
	s_list = pd.read_csv("./data/pm_info.csv")
	res = []
	for i in s_list['symptoms']:
		if i in ll:
			res.append(1)
		else:
			res.append(0)
	return res

def saveamfeedback(pig_farm_address="", farm_phone_no="", email_address="", animal_no="", date_of_sikness="", symptoms="", score="", disease_by_vet="", satisfaction="", suggestion=""):
	df_feedback = pd.read_csv("./data/am_feedback.csv")
	df_feedback = df_feedback.append({'pig_farm_address': pig_farm_address, 'farm_phone_no':farm_phone_no, 'email_address':email_address,
		'animal_no':animal_no,'date_of_sikness':date_of_sikness,'symptoms':symptoms,'score':score, 'disease_by_vet':disease_by_vet,
		'satisfaction':satisfaction, 'suggestion':suggestion}, ignore_index=True)
	df_feedback.to_csv("./data/am_feedback.csv", index=False)

def savepmfeedback(pig_farm_address="", farm_phone_no="", email_address="", animal_no="", date_of_sikness="", symptoms="", score="", disease_by_vet="", satisfaction="", suggestion=""):
	df_feedback = pd.read_csv("./data/pm_feedback.csv")
	df_feedback = df_feedback.append({'pig_farm_address': pig_farm_address, 'farm_phone_no':farm_phone_no, 'email_address':email_address,
		'animal_no':animal_no,'date_of_sikness':date_of_sikness,'symptoms':symptoms,'score':score, 'disease_by_vet':disease_by_vet,
		'satisfaction':satisfaction, 'suggestion':suggestion}, ignore_index=True)
	df_feedback.to_csv("./data/pm_feedback.csv", index=False)


def am_diseases_predict_engine(ll):
	df = pd.read_csv('./data/am.csv')
	# df.drop(['Probable_agent'], axis=1, inplace=True)	
	labelEncoder = preprocessing.LabelEncoder()
	if df['Probable_disease'].size > 0:
		labelEncoder.fit(df['Probable_disease'])
	df['Probable_disease']=labelEncoder.transform(df['Probable_disease'])
	X, y = shuffle(df.iloc[:,:-3],df.Probable_disease, random_state=13)
	model_svm = SVC(C=26, gamma=0.01, kernel='rbf', probability=True)
	model_svm.fit(X,y)
	prob_list = model_svm.predict_proba([ll])
	mx = max(prob_list[0])
	mn = min(prob_list[0])
	for index, value in enumerate(prob_list[0]):
		x= (value-mn)*9
		y=(x/(mx-mn))+1
		prob_list[0][index]=y
	score_list = sorted(prob_list[0], reverse=True)
	score_list = np.round(score_list)
	pred = (-model_svm.predict_proba([ll])).argsort()[0]
	return labelEncoder.inverse_transform(pred[:3]), adjusting(score_list[:3])

def pm_diseases_predict_engine(ll):
<<<<<<< HEAD
	df = pd.read_csv('./data/pm.csv')
=======
	df = pd.read_csv('data/pm.csv')
>>>>>>> 1a5e23280bfdba7447c0c53d28fb93b9614f950d
	df.drop(['Probable_agent','Approve','Partial','Total','Decision'], axis=1, inplace=True)
	labelEncoder = preprocessing.LabelEncoder()
	if df['Probable_disease'].size > 0:
		labelEncoder.fit(df['Probable_disease'])
	df['Probable_disease']=labelEncoder.transform(df['Probable_disease'])
	X, y = shuffle(df.iloc[:,:-1],df.Probable_disease, random_state=13)
	model_svm = SVC(C=10, gamma=0.1, kernel='sigmoid', probability=True)
	model_svm.fit(X,y)
	prob_list = model_svm.predict_proba([ll])
	mx = max(prob_list[0])
	mn = min(prob_list[0])
	for index, value in enumerate(prob_list[0]):
		x= (value-mn)*9
		y=(x/(mx-mn))+1
		prob_list[0][index]=y
	score_list = sorted(prob_list[0], reverse=True)
	score_list = np.round(score_list)
	pred = (-model_svm.predict_proba([ll])).argsort()[0]
	return labelEncoder.inverse_transform(pred[:3]), adjusting(score_list[:3])



def am_decision_predict_engine(ll,st):
	df = pd.read_csv('./data/am.csv')
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

def pm_decision_predict_engine(ll,st):
	df = pd.read_csv('./data/pm.csv')
	df.drop(['Probable_agent','Approve','Partial','Total'], axis=1, inplace=True)
	dcle = preprocessing.LabelEncoder()
	pdle = preprocessing.LabelEncoder()
	if df['Probable_disease'].size > 0:
		pdle.fit(df['Probable_disease'])
	if df['Decision'].size > 0:
		dcle.fit(df['Decision'])
	df['Probable_disease']=pdle.transform(df['Probable_disease'])
	df['Decision']=dcle.transform(df['Decision'])
	X, y = shuffle(df.iloc[:,:-1],df.Decision, random_state=13)
	model_svm_for_pm = SVC(C=0.1, gamma=0.01, kernel='linear')
	model_svm_for_pm.fit(X,y)
	ss = pdle.transform([st])
	ll.extend(ss)
	pred = model_svm_for_pm.predict([ll])[0]
	return dcle.inverse_transform(pred)

