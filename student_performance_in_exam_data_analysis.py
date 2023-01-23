# -*- coding: utf-8 -*-
"""Student Performance in exam -Data Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/174rrlUhpn8867axx6PvTVU9c7-n9VuVG
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data= pd.read_csv("StudentsPerformance.csv")
data.head()

data.shape

data.isnull().sum()

data.dtypes

data.info()

data["gender"].value_counts()

data["race/ethnicity"].value_counts()

data["parental level of education"].value_counts()

data["lunch"].value_counts()

data["test preparation course"].value_counts()

data["total"] = data["math score"]+data["reading score"]+data["writing score"]
data["average"] = data["total"]/3

data.head()

data.tail()

sns.displot(data["math score"])

sns.displot(data["reading score"])

sns.displot(data["writing score"])

sns.displot(data["average"])

sns.pairplot(data)

sns.barplot(data["race/ethnicity"],data['average'])

sns.barplot(data["parental level of education"],data['average'])

sns.barplot(data["test preparation course"],data['average'])

data['math_PassStatus'] = np.where(data['math score'] < 40,'F','P')
data['reading_PassStatus'] = np.where(data['reading score'] < 40,'F','P')
data['writing_PassStatus'] = np.where(data['writing score'] < 40,'F','P')

data['math_PassStatus'].value_counts()

data['reading_PassStatus'].value_counts()

data['writing_PassStatus'].value_counts()

p = sns.countplot(x='parental level of education', data = data, hue='math_PassStatus', palette ='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)

p = sns.countplot(x='test preparation course', data = data, hue='math_PassStatus', palette ='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)

p = sns.countplot(x='parental level of education', data = data, hue='reading_PassStatus', palette ='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)

p = sns.countplot(x='test preparation course', data = data, hue='reading_PassStatus', palette ='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)

p = sns.countplot(x='parental level of education', data = data, hue='writing_PassStatus', palette ='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)

p = sns.countplot(x='test preparation course', data = data, hue='writing_PassStatus', palette ='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)

sns.set(style='whitegrid')

plt.figure(figsize=(14, 7))
labels=['Female', 'Male']
plt.pie(data['gender'].value_counts(),labels=labels,explode=[0.1,0.1],
        autopct='%1.2f%%',colors=['#E37383','#FFC0CB'], startangle=90)
plt.title('Gender')
plt.axis('equal')
plt.show()