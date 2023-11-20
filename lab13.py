#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
df = pd.read_csv("Iris.csv")
df.head()


# In[19]:


df.info()


# In[20]:


df.describe


# In[21]:


df.isnull().sum()


# In[22]:


df.value_counts("Species")


# In[23]:


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Species', data=df, )
plt.show()


# In[26]:


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm',
hue='Species', data=df, )
plt.show()


# In[28]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm',
hue='Species', data=df, )
plt.show()


# In[31]:


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 2, figsize=(10,10))
axes[0,0].set_title("sepal Length")
axes[0,0].hist(df['SepalLengthCm'], bins=7)
axes[0,1].set_title("sepal width")
axes[0,1].hist(df['SepalWidthCm'], bins=5);
axes[1,0].set_title("Petal Length")
axes[1,0].hist(df['PetalLengthCm'], bins=6);
axes [1,1].set_title("Petal Width")
axes[1,1].hist(df['PetalWidthCm'], bins=6);


# In[35]:


df.corr()


# In[36]:


sns.heatmap(df.corr(), annot = True);
plt. show()


# In[ ]:




