#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### print data.shape
### print np.size ( data, 0 )
### label, features = targetFeatureSplit ( data )

### your code below

max_salary = np.amax ( data, axis=0 )[0]
max_bonus  = np.amax ( data, axis=0 )[1]
index_max_salary = np.argmax ( data, axis=0 )[0]
index_max_bonus  = np.argmax ( data, axis=0 )[1]
print "INDEX Maximum Salary =", index_max_salary, "INDEX Maximum Bonus =", index_max_bonus
print "Maximum Salary =", max_salary, "Maximum Bonus =", max_bonus

keys = data_dict.keys()
for key in keys:
   salary_test = data_dict[key]["salary"]
   bonus_test = data_dict[key]["bonus"]
   if ( salary_test == max_salary ):
      print "Person =", key, "Salary =", salary_test, "Bonus =", bonus_test

# feature_list = ["poi", "salary", "bonus"] 
# data_array = featureFormat( data_dict, feature_list )
# label, features = targetFeatureSplit(data_array)

### count = 0
## for i in data_dict.keys():
##    print count, i
##    count += 1

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

