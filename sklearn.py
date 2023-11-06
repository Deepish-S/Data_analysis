#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[17]:


df=pd.read_csv('lab11.csv')


# In[19]:


x = df.drop('price', axis='columns')
x=x.values
x


# In[20]:


price = df.price
price


# In[21]:


reg = linear_model. LinearRegression()
reg.fit(x,price)


# In[25]:


reg.predict([[3000]])


# In[26]:


reg.coef_


# In[27]:


reg.intercept_


# In[29]:


print(reg.coef_* 3000+reg.intercept_)


# In[ ]:




