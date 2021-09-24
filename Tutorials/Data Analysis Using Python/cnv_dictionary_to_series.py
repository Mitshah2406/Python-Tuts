#!/usr/bin/env python
# coding: utf-8

# In[12]:


#converting dictionaries into series
from pandas import Series
salary = {'Rob':4500,'Mit':2500000,'Adi':2500000}
se = Series(salary)
se


# In[13]:


se['Mit']


# In[ ]:




