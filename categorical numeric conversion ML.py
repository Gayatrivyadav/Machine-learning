#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[37]:


data1 = pd.read_csv("C:/Users/Gayatri/Downloads/archive (11)/Salary Data.csv")


# In[38]:


data1.head()


# In[39]:


data1.isna().sum()


# In[40]:


data1.info()


# In[41]:


data1["Age"] = data1["Age"].mean()


# In[ ]:





# In[42]:


data1["Years of Experience"] = data1["Years of Experience"].mean()


# In[43]:


data1["Salary"] = data1["Salary"].mean()


# In[44]:


data1.isna().sum()


# In[45]:


data1["Gender"].replace(['Male', 'Female'],
                        [0, 1], inplace=True)


# In[46]:


data1.head()


# In[47]:


df1 = pd.get_dummies(data1['Education Level'])


# In[48]:


data1 = pd.concat([data1, df1], axis=1).reindex(data1.index)


# In[49]:


data1.head()


# In[34]:


data1.drop("Education Level", axis = 1, inplace = True)


# In[35]:


data1.head()


# In[1]:


# X = data1[["Years of Experience"]]


# In[2]:


# from sklearn.preprocessing import StandardScaler 
# scaler = StandardScaler()


# In[3]:


# print(scaler.fit_transform(X)[:3, :]) 


# In[4]:


# scaler.mean_


# In[ ]:




