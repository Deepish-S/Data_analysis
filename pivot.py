#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df=pd.read_csv('titanic.csv')


# In[9]:


df.head(5)


# In[10]:


table = pd.pivot_table(df, index=['Sex', 'Pclass'], aggfunc={'Survived':np.sum})
table


# In[11]:


table = pd.pivot_table(df,index=['Sex', 'Pclass'], values=['Survived'], aggfunc=np.mean)
table


# In[12]:


table.plot(kind='bar');


# In[13]:


table = pd.pivot_table(df, index=['Sex'], columns=['Pclass'], values=['Survived'], aggfunc=np. sum)
table


# In[14]:


table.plot(kind='bar');


# In[ ]:




