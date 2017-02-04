#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2, f3 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kmeans = KMeans ( n_clusters=2, random_state=0).fit(data)
pred = kmeans.predict ( data )

max_salary = np.amax ( data, axis=0 )[0]
max_bonus  = np.amax ( data, axis=0 )[1]
index_max_salary = np.argmax ( data, axis=0 )[0]
index_max_bonus  = np.argmax ( data, axis=0 )[1]
print "INDEX Maximum Salary =", index_max_salary, "INDEX Maximum Bonus =", index_max_bonus
print "Maximum Salary =", max_salary, "Maximum Bonus =", max_bonus

keys = data_dict.keys()
MIN_exercised_stock_options = sys.float_info.max
MAX_exercised_stock_options = sys.float_info.min
for key in keys:
   exercised_stock_options_test = data_dict[key]["exercised_stock_options"]
   if ( exercised_stock_options_test != "NaN" ) and ( exercised_stock_options_test > 0 ):
      if ( exercised_stock_options_test < MIN_exercised_stock_options ):
         MIN_exercised_stock_options = exercised_stock_options_test
      if ( exercised_stock_options_test > MAX_exercised_stock_options ):
          MAX_exercised_stock_options = exercised_stock_options_test

print "Minimum Exercised Stock Option =", MIN_exercised_stock_options, "Maximum Exercised Stock Option =", MAX_exercised_stock_options

keys = data_dict.keys()
MIN_salary = sys.float_info.max
MAX_salary = sys.float_info.min
for key in keys:
   salary_test = data_dict[key]["salary"]
   if ( salary_test != "NaN" ) and ( salary_test > 0 ):
      if ( salary_test < MIN_salary ):
         MIN_salary = salary_test
      if ( salary_test > MAX_salary ):
          MAX_salary = salary_test

print "Minimum Salary =", MIN_salary, "Maximum Salary =", MAX_salary


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    ### Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters_3.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
