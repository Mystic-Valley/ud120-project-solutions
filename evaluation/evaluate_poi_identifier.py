#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.metrics import accuracy_score as acc
clf = DT()
clf.fit(features, labels)
print acc(clf.predict(features), labels)

from sklearn.model_selection import  train_test_split
features_train, features_test, labels_train , labels_test = train_test_split(features, labels, test_size = 0.3,  random_state = 42 )
clf2 = DT()
clf2.fit(features_train, labels_train)
pred = clf2.predict(features_test)
print acc(pred, labels_test)

#no of poi
print labels_test

#no of people in test set
print len(labels_test)

print pred
print labels_test

from  sklearn.metrics import precision_score, recall_score
print precision_score(labels_test, pred)
print recall_score(labels_test, pred)