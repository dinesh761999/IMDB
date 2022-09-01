#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as ny
import seaborn as sns


# In[8]:


data = pd.read_csv('c:/Users/DINESH/Music/IMDB_Movie.csv')


# In[ ]:


# Display Top Row of the dataset


# In[9]:


data.head()


# In[ ]:


# Check Last Rows of The Dataset


# In[10]:


data.tail()


# In[ ]:


# Find Shape of Our Dataset


# In[11]:


data.shape


# In[12]:


data.describe()


# In[13]:


data.columns


# In[14]:


data.nunique()


# In[ ]:


# Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement


# In[15]:


data.info()


# In[ ]:


# Check Missing Values In The Datase


# In[16]:


data.isnull().sum()


# In[17]:


sns.heatmap(data.isnull())


# In[ ]:


# Drop All The  Missing Values


# In[18]:


data.dropna(axis=0)


# In[ ]:


# Check For Duplicate Data


# In[19]:


data.duplicated().any()


# In[20]:


data=data.drop_duplicates()
data


# In[ ]:


# Get Overall Statistics About The DataFrame


# In[21]:


data.describe(include='all')


# In[ ]:


# Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes


# In[22]:


data.columns


# In[23]:


data[data['Runtime (Minutes)']>=180]['Title']


# In[ ]:


# In Which Year There Was The Highest Average Voting?


# In[78]:


data.columns


# In[24]:


data.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[25]:


sns.barplot(x='Year',y='Votes',data=data)


# In[ ]:


# In Which Year There Was The Highest Average Revenue?


# In[26]:


data.columns


# In[27]:


data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[28]:


sns.barplot(x='Year',y='Revenue (Millions)',data=data)


# In[ ]:


# Find The Average Rating For Each Director


# In[29]:


data.columns


# In[30]:


data.groupby('Director')['Rating'].mean().sort_values(ascending=False)


# In[ ]:


# Display  Movies Title and Runtime ( highest time)


# In[31]:


data.columns


# In[32]:


data.groupby('Title')['Runtime (Minutes)'].mean().sort_values(ascending=False)


# In[ ]:


# Display Top 10 Lengthy Movies Title and Runtime


# In[33]:


Top10_len=data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']].set_index('Title')


# In[34]:


Top10_len


# In[35]:


sns.barplot(x='Runtime (Minutes)',y=Top10_len.index , data=Top10_len)


# In[ ]:


# Display Number of Movies Per Year


# In[36]:


data.columns


# In[37]:


data['Year'].value_counts()


# In[38]:


sns.countplot(x='Year',data=data)


# In[39]:


data.columns


# In[40]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title']


# In[ ]:


# Display Top 10 Highest Rated Movie Titles And its Directors


# In[41]:


data.columns


# In[42]:


Top10_len=data.nlargest(10,'Rating')[['Title','Director','Rating']].set_index('Title')


# In[43]:


Top10_len


# In[44]:


sns.barplot(x='Rating',y=Top10_len.index,data=Top10_len , hue='Director', dodge=False)
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# In[ ]:


#      Display Top 10 Highest Revenue Movie Titles


# In[47]:


data.columns


# In[48]:


data.nlargest(10,'Revenue (Millions)')['Title']


# In[49]:


top_10=data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')


# In[50]:


top_10


# In[51]:


sns.barplot(x='Revenue (Millions)', y =top_10.index, data=top_10)


# In[ ]:


# Find Average Rating of Movies Year Wise


# In[52]:


data.columns


# In[53]:


data.groupby('Year')['Rating'].mean().sort_values(ascending=False)


# In[ ]:


# Does Rating Affect The Revenue?


# In[54]:


sns.scatterplot(x='Rating', y='Revenue (Millions)', data=data)


# In[ ]:


# Classify Movies Based on Ratings [Excellent, Good, and Average]


# In[55]:


data.columns


# In[56]:


def rating(rating):
    if rating>=7.0:
        return'Excellent'
    elif rating>=6.0:
         return'Good'
    else:
        return'Average'


# In[58]:


data.head()


# In[57]:


data['rating_cat']=data['Rating'].apply(rating)


# In[ ]:


# Count Number of Action Movies


# In[59]:


data.columns


# In[60]:


data['Genre'].dtype


# In[61]:


len(data[data['Genre'].str.contains('Action',case=False)])


# In[ ]:


# Find Unique Values From Genre


# In[62]:


data.columns


# In[63]:


data['Genre']


# In[64]:


list1=[]
for value in data ['Genre']:
    list1.append(value.split (','))


# In[65]:


list1


# In[66]:


one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# In[67]:


one_d


# In[ ]:


# Find Unique Values From Genremm


# In[68]:


uni_list=[]
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)


# In[69]:


uni_list


# In[ ]:


# How Many Films of Each Genre Were Made?


# In[70]:


one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# In[71]:


one_d


# In[ ]:


from collections import counter


# In[ ]:


counter(one_d)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




