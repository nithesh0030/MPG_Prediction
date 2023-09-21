#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np



# In[25]:


mpg_df=pd.read_csv("Auto MPG Reg.csv")


# In[26]:


mpg_df.horsepower=mpg_df.horsepower.fillna(mpg_df.horsepower.median())


# In[27]:


y=mpg_df.mpg
x=mpg_df.drop('mpg',axis=1)


# In[28]:


from sklearn.linear_model import LinearRegression


# In[29]:


reg=LinearRegression()


# In[36]:


reg.fit(x,y)


# In[37]:


reg.score(x,y)


# In[38]:


regpred = reg.predict(x)


# In[39]:


from sklearn.metrics import mean_squared_error


# In[40]:


np.sqrt(mean_squared_error(y,regpred))






