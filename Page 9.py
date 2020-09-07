#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[6]:


grades = [76,95,77,78,99]


# In[7]:


bsdegrees = [1,1,0,0,1]


# In[8]:


msdegrees = [2,1,0,0,0]


# In[9]:


phddegrees = [0,1,0,0,0]


# In[10]:


Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)


# In[11]:


columns = ['Names','Grades','BS','MS','PHD']


# In[12]:


df = pd.DataFrame(data = Degrees, columns=column)


# In[13]:


df


# In[ ]:




