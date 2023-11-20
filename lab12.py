#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
titanic = pd.read_csv('titanic.csv')
titanic.head(5)


# In[2]:


titanic.isnull().sum()


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt
# Countplot
sns.catplot(x ="Sex", hue ="Survived", kind ="count", data = titanic)


# In[7]:


group = titanic.groupby(['Pclass', 'Survived'])
pclass_survived = group.size().unstack()
sns.heatmap(pclass_survived, annot = True, fmt ="d")


# In[8]:


sns.catplot(x ='Embarked', hue ='Survived',
kind ='count', col ='Pclass', data = titanic)


# In[9]:


# Divide Fare into 4 bins
titanic['Fare_Range'] = pd.qcut(titanic['Fare'], 4)
# Barplot - Shows approximate values based
# on the height of bars.
sns.barplot(x ='Fare_Range', y ='Survived',
data = titanic)


# In[13]:


sns.violinplot(x ="Sex", y ="Age", hue ="Survived",
data = titanic, split = True)


# In[ ]:




