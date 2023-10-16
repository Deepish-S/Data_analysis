#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd


# In[26]:


df = pd.read_excel('lab8.xlsx')


# In[27]:


df


# In[28]:


df.dtypes 


# In[29]:


df.drop_duplicates(inplace=True)
df


# In[30]:


df.dropna(inplace=True)
df


# In[31]:


df['B'] = df['B'].str.lower()
df


# In[32]:


df= df.apply(lambda x: x.str.replace(r'[\\n]',' ', regex=True).str.strip())
df


# In[34]:


df = df.apply(lambda x: x.str.replace(r'[^a-zA-Z0-9\s]', '', regex=True))
df


# In[ ]:




