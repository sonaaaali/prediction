# -*- coding: utf-8 -*-
"""Crimedetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mu0KIj4hEwhn4rjklOHzQgEPJfR64Qmv
"""

import pandas as pd

df = pd.read_table("/content/DATABASE - Sheet1.csv",sep = ",")
df

df.info()

df.head()

y = df['Unnamed: 3'].values
y
loc = df['Unnamed: 6'].values 
loc[0] = 'chennai'
locationarray = []
for city in loc:
  locationarray.append(city.lower())
locationarray

y[0] = 'Crime'
y

inputstring = 'i would like to report a crime... There was a Murder at tnagar at 2:00am on 06/07/2018'
crimekeyword = []
crimekeywordininput = []
for word in y:
  crimekeyword.append(word)
inputstringarray = inputstring.split(" ")
for word in inputstringarray:
  if word in crimekeyword:
    print(word)
    crimekeywordininput.append(word)



locationkeywordinput = []
for word in inputstringarray:
  if word.lower() in locationarray:
    print(word)
    locationkeywordinput.append(word)
locationkeywordinput

firlist = ['Date - 20/06/2018 time - 5:00pm   place - Ramapuram Incident details - Man killed daughters friend with a wooden log in a fit of rage.','Date - 06/07/2018 time - 2:00am Place - Tnagar Incident details - Incident took place at the vicitims home. Many valuables were stolen.' ]
firarray = []
for sentence in firlist:
  firword = sentence.split(" ")
for element in firword:
  firarray.append(element.lower())
firarray
firdates = ['20/06/2018','06/07/2018','07/07/2018','06/08/2018','09/12/2018']
firtimes = ['5:00pm','2:00am','8:00pm','2:00pm','11pm']

crimecomfirm = 0
placecomfirm = 0
timecomfirm = 0
datecomfirm = 0

for x in crimekeywordininput:
  if x in firarray:
    crimecomfirm =1
for x in locationkeywordinput:
  if x in firarray:
    placecomfirm = 1
    print(x)
for x in inputstringarray:
  if x in firdates:
    print(x)
    datecomfirm = 1
for x in inputstringarray:
  if x in firtimes:
    timecomfirm = 1
    print(x)
print(timecomfirm,datecomfirm,placecomfirm,crimecomfirm)

import matplotlib.pyplot as plt
import numpy as np

if crimekeywordininput == 'Terrorist attack' and placecomfirm == 0 and datecomfirm == 0 and timecomfirm == 0:
  average = 0
else:
  average = (crimecomfirm+placecomfirm+datecomfirm+timecomfirm)/4


y = np.array([ average,1-average])
mylabels = ["Legit","Fake"]
mycolors = ["green","orange"]
myexplode = [0.2,0]
plt.pie(y,labels = mylabels,colors = mycolors, explode = myexplode, shadow = True,autopct='%1.2f%%')
plt.legend()
plt.show()