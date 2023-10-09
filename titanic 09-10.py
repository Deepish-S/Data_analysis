#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df = pd.read_csv("titanic_dataset.csv")
df


# In[3]:


df.head (10)


# In[4]:


df. tail(1e)


# In[5]:


df. tail(10)


# In[7]:


df.describe()


# In[12]:


df.isnull().sum()


# In[13]:


df['Fare'].mean()


# In[14]:


df['Fare'].median()


# In[15]:


df['Fare'].mode()


# In[16]:


df['Fare'].std()


# In[17]:


df['Fare'].var()


# In[ ]:





# In[ ]:





# In[9]:


df['Sex'].value_counts()


# In[10]:


df['Sex'].value_counts(ascending = True)


# In[11]:


df['Fare'].value_counts().max


# In[19]:


df['Cabin'].value_counts()


# In[20]:


df['Embarked'].value_counts()


# In[ ]:




