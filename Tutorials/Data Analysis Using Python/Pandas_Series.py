#!/usr/bin/env python
# coding: utf-8

# In[7]:


#PAndas is a librrary used for data analysis
#it has two data structures as Series And DataFrames
#Series
from pandas import Series
se = Series([2,3,4,5])#defining series
se #printing series


# In[3]:


se[2]#printing a particuar item in series


# In[8]:


se2 = Series([200,400,600],index = ['a','b','c'])#defining our index number in series


# In[9]:


se2


# In[10]:


se2['b']


# In[ ]:




