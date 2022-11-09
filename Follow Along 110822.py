#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import packages
import numpy as np
import pandas as pd
import os # used to handle some of the paths when downloading data via python
import urllib # used to access websites and download data from the web
get_ipython().run_line_magic('matplotlib', 'inline # allows Jupyter Notebook to be able to render plots in the notebook itself')
import matplotlib.pyplot as plt


# In[2]:


# create variables to get the data from the url and store it on the computer
url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join("data","covid")


# In[3]:


# make directories, makes folders, creates CSV path for downloaded data. This helps access the data
os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path,"WHO-COVID-19-global-data.csv")
urllib.request.urlretrieve(url,csv_path)


# In[4]:


# create a dataframe which contains the downloaded data
df = pd.read_csv(csv_path)


# In[5]:


df


# In[6]:


# create a variable which accesses the index of the dataframe
df_index = df.index
df_index


# In[7]:


# create another variable for the index of columns
df_cols = df.columns
df_cols


# In[8]:


# return values as a numpy array
df_index.values


# In[9]:


# look at the values in the dataframe, itself, presented as a numpy array
df.values


# In[11]:


# look at the datatypes
# NOTE: object refer to strings and int64 refers to integers
df.dtypes


# In[13]:


# look at the "shape" of the dataset --> number of rows, columns
df.shape


# In[14]:


# show the first five (default) entries in the dataframe, if you want more or less, pass an integer in the ()
df.head()


# In[16]:


# show the last five (default) entries in the dataframe, can also pass an integer in the () to show more/less
df.tail()


# In[17]:


# give information about the dataframe itself
df.info()


# In[19]:


# for numberic columns we get some simple statistics
df.describe()


# In[20]:


# look at a particular column in the dataframe
df["Country"]


# In[23]:


# look at only unique country names
df["Country"].unique()


# In[24]:


# use the below code to remove spaces in column names, can now use dot . notation instead of bracket [] notation
df.columns = [col.strip() for col in df.columns]
df.columns


# In[25]:


df.Country


# In[27]:


# locate specific information that we want --> [row indexer, column indexer]
df.loc[1:4,'Country']


# In[28]:


# want to look at two columns, as a list
df.loc[1:8,["Country","New_cases"]]


# In[29]:


# looking at one country with the double == creates a boolean test, selects True where Country = USA
df.Country == 'United States of America'


# In[30]:


# put the test from above inside brackets to print the true cases
df[df.Country == "United States of America"]


# In[31]:


# creates a list where new deaths > 1000
df[df.New_deaths > 1000]


# In[32]:


# combine with loc to find where new deaths are > 1000, and print with # deaths and Country as a list
df.loc[df.New_deaths > 1000, ['New_deaths','Country']]


# In[45]:


# chain conditions where new deaths are > 1000, and country is specifically the US, with a list that includes \ 
#con't: Date reported, country, new cases, new deaths, cumulative deaths as a list
df.loc[(df.New_deaths > 1000) & (df.Country_code == 'US'),        ['Date_reported','Country','New_cases','New_deaths','Cumulative_deaths']]


# In[46]:


# return the max number of new cases for the US
df.loc[df.Country_code == 'US', ['New_cases']].max()


# In[47]:


# return the minimum number of new cases for the US
df.loc[df.Country_code == 'US', ['New_cases']].min()


# In[48]:


# sum the new cases in the US (should be equal to the number of cumulative cases in the US)
df.loc[df.Country_code == "US", ['New_cases']].sum()


# In[49]:


# check if the above hypothesis is true by getting the max number of cumulative cases
df.loc[df.Country_code == 'US', ['Cumulative_cases']].max()


# In[51]:


# looking at the new_deaths column, return the index number of the maximum entry
df.New_deaths.idxmax()


# In[52]:


# using the idxmax from above, make a full list of information
df.loc[df.New_deaths.idxmax(), ['Date_reported','Country','New_cases','New_deaths','Cumulative_deaths']]


# In[53]:


# look where new deaths are less than 0
df[df.New_deaths < 0]


# In[64]:


# create new columns just by giving them a name and creating the conditions
# create a new column of percent cases by dividing new cases by cumulative cases
df['pct_cases'] = (df['New_cases'] / df['Cumulative_cases']) * 100
df


# In[65]:


# filter out new_deaths under 1000
df.loc[df.New_deaths > 1000]


# In[72]:


# create a variable that stores the above table
table_1 = df.loc[df.New_deaths > 10000]
table_1


# In[88]:


# plot a bar graph of table 1 where x axis is country and y axis is pct cases
table_1.plot(x = 'Country', y = 'pct_cases', kind = 'bar', figsize = (9,8))
plt.show()


# In[85]:


# create a table_2 for just the united states where new deaths are over 10,000
table_2 = df.loc[(df.New_deaths > 10000) & (df.Country_code == 'US')]
table_2


# In[103]:


# create a bar graph showing this table with dates on the x axis and pct on the y
table_2.plot(x = 'Date_reported', y = 'pct_cases', kind = 'bar', figsize = (6,4))

plt.title('Percent of COVID cases in the United States on days when new deaths were over 10,000')
plt.xlabel('Date')
plt.ylabel('Percent Cases')


plt.show()


# In[109]:


# using the same data, plot the dates and number of new deaths instead of pct
table_2.plot(x = 'Date_reported', y = 'New_deaths', kind = 'bar', figsize = (6,4))

plt.title('Deaths over 10,000 reported in the United States')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.legend('', frameon = False) # removes legend

plt.show()


# In[ ]:




