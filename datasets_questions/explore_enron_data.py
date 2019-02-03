#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:
    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000    
"""

import pickle

poi_list = open("../final_project/poi_names.txt", "r")
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# for i in sorted(enron_data):
#     print i

# for i in sorted(enron_data):
#     print enron_data[i]


# print len(enron_data)

# print len(enron_data['GLISAN JR BEN F'])

# count  = 0
# for i in range(len(enron_data)):
#     d = enron_data.values()
#     if d[i]['poi'] == 1:
#         count += 1
# print count

for i in poi_list:
    print i
# print len(list(poi_list))

# print enron_data["PRENTICE JAMES"]['total_stock_value']

# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

# print enron_data['LAY KENNETH L']['total_payments']
# print enron_data['SKILLING JEFFREY K']['total_payments']
# print enron_data['FASTOW ANDREW S']['total_payments']

# count  = 0
# for i in enron_data:
#     if enron_data[i]['salary'] != "NaN":
#         count += 1
# print count
# count  = 0
# for i in enron_data:
#     if enron_data[i]['email_address'] != "NaN":
#         count += 1
# print count

count  = 0
for i in enron_data:
    if enron_data[i]['total_payments'] == "NaN":
        count += 1
print count
print float(count)/len(enron_data.keys())

# count = 0
# for i in enron_data.keys():
#     if enron_data[i]['total_payments'] == 'NaN' and enron_data[i]['poi'] == True :
#         print 
#         count += 1
# print count
# print float(count)/len(enron_data.keys())