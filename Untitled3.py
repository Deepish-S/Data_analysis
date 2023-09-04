#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv("tem.csv")


# In[4]:


df


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[7]:


df.head(2)


# In[8]:


df.isnull()


# In[9]:


df.isnull().sum()


# In[10]:


df.count()


# In[11]:


df.info()


# In[13]:


gk=df.groupby('city')
gk=gk.get_group('Mumbai')
gk


# In[ ]:




