#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

data_dict.pop('TOTAL', 0)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for i,j in data_dict.items():
    if j['bonus'] == data.max():
        print i

for person in data_dict.keys():
	if type(data_dict[person]["bonus"]) is int and data_dict[person]["salary"] >= 1000000 and data_dict[person]["bonus"] >= 5000000 :
		print person, data_dict[person]["bonus"]
