#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[71]:


df=pd.read_csv('lab11.csv')


# In[72]:


df.head(5)


# In[73]:


x = df.drop('price', axis='columns')
x=x.values
x


# In[74]:


price = df.price
price


# In[75]:


reg=linear_model.LinearRegression()
reg.fit(x,price)


# In[76]:


reg.predict([[60]])


# In[77]:


print(reg.coef_* 60+reg.intercept_)


# In[78]:


reg.coef_


# In[79]:


reg.intercept_


# In[80]:


print(reg.coef_* 3000+reg.intercept_)


# In[ ]:




