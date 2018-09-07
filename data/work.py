import numpy as np
import pandas as pd

table1 = pd.read_csv("am.csv")
table2 = pd.read_csv("pm.csv")
table3 = pd.read_csv("disease_info.csv")
table4 = pd.read_csv("am_info.csv")
table5 = pd.read_csv("pm_info.csv")
st =""

# for i in sorted(table1.Probable_disease.unique(), key=str.lower):
# 	print(i)

# for i in sorted(table2.Probable_disease.unique(), key=str.lower):
# 	print(i)

# for i in sorted(table3.Disease.unique(), key=str.lower):
# 	print(i)


first_list = sorted(table1.Probable_disease.unique(), key=str.lower)
second_list = sorted(table2.Probable_disease.unique(), key=str.lower)
# resultList= sorted(list(set(first_list)|set(second_list)), key=str.lower)
# for i in resultList:
# 	print(i)

# for i in second_list:
# 	st=st+str(i)+', '
# 	# print(i)
# print(st)
print(len(second_list))