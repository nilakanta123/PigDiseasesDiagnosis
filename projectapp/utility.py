import numpy as np
import pandas as pd

def get_symptom_list():
	res = {}
	s_list = pd.read_csv("data/info.csv")
	# res['age'] =s_list[0:6]
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
