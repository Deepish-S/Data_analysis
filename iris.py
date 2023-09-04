#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("iris.csv")


# In[3]:


df


# In[4]:


df.shape


# In[6]:


df.dtypes


# In[7]:


df.head(3)


# In[8]:


df.tail(3)


# In[9]:


df.isnull()


# In[10]:


df.info()


# In[15]:


gk=df.groupby('variety')
gk=gk.get_group('Setosa')
gk


# In[ ]:




