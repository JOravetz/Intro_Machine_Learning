
## Explore Enron Data Excercise
Joseph J. Oravetz


```python
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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# How many POIs are there in the E+F dataset
count = 0
for i in range(len(enron_data)):
    a = enron_data.values()
    if a[i]['poi'] == True:
        count = count + 1        
print count

```

    18



```python
### how many data points (People) are in the dataset?
print "Number of data points (People) in the dataset = %d" % len ( enron_data )
### print len ( enron_data.keys () )
```

    Number of data points (People) in the dataset = 146



```python
#### For each person, how many features are available?
print "For each person, how many features are available? = %d" % len(enron_data.values()[0])
print enron_data[enron_data.keys()[0]]
### print len(enron_data['SKILLING JEFFREY K'])
```

    For each person, how many features are available? = 21
    {'salary': 365788, 'to_messages': 807, 'deferral_payments': 'NaN', 'total_payments': 1061827, 'exercised_stock_options': 'NaN', 'bonus': 600000, 'restricted_stock': 585062, 'shared_receipt_with_poi': 702, 'restricted_stock_deferred': 'NaN', 'total_stock_value': 585062, 'expenses': 94299, 'loan_advances': 'NaN', 'from_messages': 29, 'other': 1740, 'from_this_person_to_poi': 1, 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN', 'email_address': 'mark.metts@enron.com', 'from_poi_to_this_person': 38}



```python
# How many POIs are there in the E+F dataset
count = 0
### print range(len(enron_data))
for i in range(len(enron_data)):
    a = enron_data.values()
    if a[i]['poi'] == True:
        count = count + 1        
print count
```

    18



```python
%%bash
cd ${HOME}/Udacity/Intro_Machine_Learning/ud120-projects/final_project
awk '{if(NF==3){print}}' poi_names.txt | wc -l
```

    35



```python
### enron_data["LASTNAME FIRSTNAME"]["feature_name"]
### enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]
### What is the total value of the stock belonging to James Prentice?
for i in range(len(enron_data)):
    ### print enron_data.keys()[i]
    if enron_data.keys()[i] == 'PRENTICE JAMES':
        total_stock_value = enron_data.values()[i]['total_stock_value']
        print "The total value of the stock belonging to James Prentice = %d" % total_stock_value
```

    The total value of the stock belonging to James Prentice = 1095040


Like any dict of dicts, individual people/features can be accessed like so:
**enron_data["LASTNAME FIRSTNAME"]["feature_name"]**

How many email messages do we have from Wesley Colwell to persons of interest?


```python
for i in range(len(enron_data)):
    #print enron_data.keys()[i]
    if enron_data.keys()[i] == 'COLWELL WESLEY':
        #print enron_data.values()[i]
        from_this_person_to_poi = enron_data.values()[i]['from_this_person_to_poi']
        print "Number of email messages from Wesley Colwell to persons of interest = %d" % from_this_person_to_poi
```

    Number of email messages from Wesley Colwell to persons of interest = 11


Like any dict of dicts, individual people/features can be accessed like so:

**enron_data["LASTNAME FIRSTNAME"]["feature_name"]**

or

**enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]**

What’s the value of stock options exercised by Jeffrey K Skilling?


```python
for i in range(len(enron_data)):
    if enron_data.keys()[i] == 'SKILLING JEFFREY K':
        #print enron_data.values()[i]
        exercised_stock_options = enron_data.values()[i]['exercised_stock_options']
        ### print "Value of stock options exercised by Jeffrey K Skilling = %d" % exercised_stock_options
        print "Value of stock options exercised by Jeffrey K Skilling = ${:,.2f}".format(exercised_stock_options)
```

    Value of stock options exercised by Jeffrey K Skilling = $19,250,000.00


Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?

How much money did that person get?


```python
for i in range(len(enron_data)):
    ### print enron_data.keys()[i]
    if enron_data.keys()[i] == 'SKILLING JEFFREY K':
        total_payments = enron_data.values()[i]['total_payments']
        print " Total Payments made to Jeffrey K Skilling = ${:,.2f}" .format(total_payments)
    if enron_data.keys()[i] == 'LAY KENNETH L':
        total_payments1 = enron_data.values()[i]['total_payments']
        print " Total Payments made to Kenneth L Lay = ${:,.2f}" .format(total_payments1)
    if enron_data.keys()[i] == 'FASTOW ANDREW S':
        total_payments2 = enron_data.values()[i]['total_payments']
        print " Total Payments made to Andrew S Fastow = ${:,.2f}" .format(total_payments2)
max_amount = float( max ( total_payments, total_payments1, total_payments2))
```

     Total Payments made to Kenneth L Lay = $103,559,793.00
     Total Payments made to Andrew S Fastow = $2,424,083.00
     Total Payments made to Jeffrey K Skilling = $8,682,716.00


How many folks in this dataset have a quantified salary? What about a known email address?


```python
count = 0
count_email = 0
for i in range(len(enron_data)):
    if enron_data.values()[i]['salary'] != 'NaN':
        ### print enron_data.values()[i]['salary']
        count += 1
    if enron_data.values()[i]['email_address'] != 'NaN':
        ### print enron_data.values()[i]['salary']
        count_email += 1
print "Number of folks in this dataset with quantified salary = %d" % count
print "Number of folks in this dataset with an email address = %d" % count_email
```

    Number of folks in this dataset with quantified salary = 95
    Number of folks in this dataset with an email address = 111


A python dictionary can’t be read directly into an sklearn classification or regression algorithm; instead, it needs a numpy array or a list of lists (each element of the list (itself a list) is a data point, and the elements of the smaller list are the features of that point).

We’ve written some helper functions **(featureFormat()** and **targetFeatureSplit()** in tools/feature_format.py) that can take a list of feature names and the data dictionary, and return a numpy array.

In the case when a feature does not have a value for a particular person, this function will also replace the feature value with 0 (zero).

As you saw a little while ago, not every POI has an entry in the dataset (e.g. Michael Krautz). That’s because the dataset was created using the financial data you can find in final_project/enron61702insiderpay.pdf, which is missing some POI’s (those absences propagated through to the final dataset). On the other hand, for many of these “missing” POI’s, we do have emails.

While it would be straightforward to add these POI’s and their email information to the E+F dataset, and just put “NaN” for their financial information, this could introduce a subtle problem. You will walk through that here.

**How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?**


```python
from __future__ import division
count = 0
total_kount = len ( enron_data )
print "Total number of people in enron_data = %d" % total_kount
for i in range(len(enron_data)):
    total_payments = enron_data.values()[i]['total_payments']
    if total_payments == 'NaN':
        count += 1
print "Total Payments with NaN values = %d" % count
percent = ( count / total_kount ) * 100.0
print "Percent of total payments having NaN values = %6.2f" % percent 
```

    Total number of people in enron_data = 146
    Total Payments with NaN values = 21
    Percent of total payments having NaN values =  14.38


How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?


```python
from __future__ import division
count = 0
total_kount = len ( enron_data )
print "Total number of people in enron_data = %d" % total_kount
for i in range(len(enron_data)):
    total_payments = enron_data.values()[i]['total_payments']
    poi = enron_data.values()[i]['poi']
    if total_payments == 'NaN' and poi == 'True':
        count += 1
print "POI and Total Payments with NaN values = %d" % count
percent = ( count / total_kount ) * 100.0
print "Percent of total payments having POI and NaN values = %6.2f" % percent 
```

    Total number of people in enron_data = 146
    POI and Total Payments with NaN values = 0
    Percent of total payments having POI and NaN values =   0.00


If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.

**What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?**


```python
### Add 10 to count and total_count variables for the question above ###
count = 10
total_kount = len ( enron_data ) + 10
print "Total number of people in enron_data = %d" % total_kount
for i in range(len(enron_data)):
    total_payments = enron_data.values()[i]['total_payments']
    if total_payments == 'NaN':
        count += 1
print "Total Payments with NaN values = %d" % count
percent = ( count / total_kount ) * 100.0
print "Percent of total payments having NaN values = %6.2f" % percent 
```

    Total number of people in enron_data = 156
    Total Payments with NaN values = 31
    Percent of total payments having NaN values =  19.87


There are now 156 folks in dataset, 31 of whom have "NaN" total_payments. This makes for 20% of them with a "NaN" overall.

***What is the new number of POI’s in the dataset? What is the new number of POI’s with NaN for total_payments?***


```python
### New number of POIs in the E+F dataset ###
count = 10
count_nan_total_payments = 10
for i in range(len(enron_data)):
    temp = enron_data.values()[i]
    if temp['poi'] == True:
        count = count + 1 
    if temp['poi'] == True and temp['total_payments'] == 'NaN':
        count_nan_total_payments += 1
print "New number of POI’s in the dataset = %d" % count
print "New number of POI’s with NaN total payments in the dataset = %d" % count_nan_total_payments
percent = ( count_nan_total_payments / count ) * 100.0
print "Percent of total payments having NaN values = %6.2f" % percent 
```

    New number of POI’s in the dataset = 28
    New number of POI’s with NaN total payments in the dataset = 10
    Percent of total payments having NaN values =  35.71


Adding in the new POI’s in this example, none of whom we have financial information for, has introduced a subtle problem, that our lack of financial information about them can be picked up by an algorithm as a clue that they’re POIs. Another way to think about this is that there’s now a difference in how we generated the data for our two classes--non-POIs all come from the financial spreadsheet, while many POIs get added in by hand afterwards. That difference can trick us into thinking we have better performance than we do--suppose you use your POI detector to decide whether a new, unseen person is a POI, and that person isn’t on the spreadsheet. Then all their financial data would contain “NaN” but the person is very likely not a POI (there are many more non-POIs than POIs in the world, and even at Enron)--you’d be likely to accidentally identify them as a POI, though!

This goes to say that, when generating or augmenting a dataset, you should be exceptionally careful if your data are coming from different sources for different classes. It can easily lead to the type of bias or mistake that we showed here. There are ways to deal with this, for example, you wouldn’t have to worry about this problem if you used only email data--in that case, discrepancies in the financial data wouldn’t matter because financial features aren’t being used. There are also more sophisticated ways of estimating how much of an effect these biases can have on your final answer; those are beyond the scope of this course.

For now, the takeaway message is to be very careful about introducing features that come from different sources depending on the class! It’s a classic way to accidentally introduce biases and mistakes.
