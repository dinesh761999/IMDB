#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd
import numpy as ny
import seaborn as sns


# In[83]:


data = pd.read_csv('c:/Users/DINESH/Music/IMDB_Movie.csv')


# In[84]:


# Display Top Row of the dataset


# In[85]:


data.head()


# In[86]:


# Check Last Rows of The Dataset


# In[87]:


data.tail()


# In[88]:


# Find Shape of Our Dataset


# In[89]:


data.shape


# In[90]:


data.describe()


# In[91]:


data.columns


# In[92]:


data.nunique()


# In[93]:


# Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement


# In[94]:


data.info()


# In[95]:


# Check Missing Values In The Datase


# In[96]:


data.isnull().sum()


# In[97]:


sns.heatmap(data.isnull())


# In[98]:


# Drop All The  Missing Values


# In[99]:


data.dropna(axis=0)


# In[100]:


# Check For Duplicate Data


# In[101]:


data.duplicated().any()


# In[102]:


data=data.drop_duplicates()
data


# In[103]:


# Get Overall Statistics About The DataFrame


# In[104]:


data.describe(include='all')


# In[105]:


# Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes


# In[106]:


data.columns


# In[107]:


data[data['Runtime (Minutes)']>=180]['Title']


# In[108]:


# In Which Year There Was The Highest Average Voting?


# In[109]:


data.columns


# In[110]:


data.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[111]:


sns.barplot(x='Year',y='Votes',data=data)


# In[112]:


# In Which Year There Was The Highest Average Revenue?


# In[113]:


data.columns


# In[114]:


data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[115]:


sns.barplot(x='Year',y='Revenue (Millions)',data=data)


# In[116]:


# Find The Average Rating For Each Director


# In[117]:


data.columns


# In[118]:


data.groupby('Director')['Rating'].mean().sort_values(ascending=False)


# In[119]:


# Display  Movies Title and Runtime ( highest time)


# In[120]:


data.columns


# In[121]:


data.groupby('Title')['Runtime (Minutes)'].mean().sort_values(ascending=False)


# In[122]:


# Display Top 10 Lengthy Movies Title and Runtime


# In[123]:


Top10_len=data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']].set_index('Title')


# In[124]:


Top10_len


# In[125]:


sns.barplot(x='Runtime (Minutes)',y=Top10_len.index , data=Top10_len)


# In[126]:


# Display Number of Movies Per Year


# In[127]:


data.columns


# In[128]:


data['Year'].value_counts()


# In[129]:


sns.countplot(x='Year',data=data)


# In[130]:


data.columns


# In[131]:


data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title']


# In[132]:


# Display Top 10 Highest Rated Movie Titles And its Directors


# In[133]:


data.columns


# In[134]:


Top10_len=data.nlargest(10,'Rating')[['Title','Director','Rating']].set_index('Title')


# In[135]:


Top10_len


# In[136]:


sns.barplot(x='Rating',y=Top10_len.index,data=Top10_len , hue='Director', dodge=False)


# In[137]:


#      Display Top 10 Highest Revenue Movie Titles


# In[138]:


data.columns


# In[139]:


data.nlargest(10,'Revenue (Millions)')['Title']


# In[140]:


top_10=data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')


# In[141]:


top_10


# In[142]:


sns.barplot(x='Revenue (Millions)', y =top_10.index, data=top_10)


# In[143]:


# Find Average Rating of Movies Year Wise


# In[144]:


data.columns


# In[145]:


data.groupby('Year')['Rating'].mean().sort_values(ascending=False)


# In[146]:


# Does Rating Affect The Revenue?


# In[147]:


sns.scatterplot(x='Rating', y='Revenue (Millions)', data=data)


# In[148]:


# Classify Movies Based on Ratings [Excellent, Good, and Average]


# In[149]:


data.columns


# In[150]:


def rating(rating):
    if rating>=7.0:
        return'Excellent'
    elif rating>=6.0:
         return'Good'
    else:
        return'Average'


# In[151]:


data.head()


# In[152]:


data['rating_cat']=data['Rating'].apply(rating)


# In[153]:


# Count Number of Action Movies


# In[154]:


data.columns


# In[155]:


data['Genre'].dtype


# In[156]:


len(data[data['Genre'].str.contains('Action',case=False)])


# In[157]:


# Find Unique Values From Genre


# In[158]:


data.columns


# In[159]:


data['Genre']


# In[160]:


list1=[]
for value in data ['Genre']:
    list1.append(value.split (','))


# In[161]:


list1


# In[162]:


one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# In[163]:


one_d


# In[164]:


# Find Unique Values From Genremm


# In[165]:


uni_list=[]
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)


# In[166]:


uni_list


# In[167]:


# How Many Films of Each Genre Were Made?


# In[168]:


one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)


# In[169]:


one_d


# In[ ]:


from collections import counter


# In[ ]:


counter(one_d)







