#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


import pandas as pd


# In[76]:


df = pd.read_csv('C:\\Users\\DIKA\\DikaPhyton\\survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('C:\\Users\\DIKA\\DikaPhyton\\survey_results_schema.csv', index_col='Column')


# In[16]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[17]:


df.shape


# In[18]:


df


# In[19]:


schema_df = pd.read_csv('C:\\Users\\DIKA\\DikaPhyton\\survey_results_schema.csv')


# In[77]:


schema_df


# In[22]:


df.head(10)


# In[24]:


person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMScgafer@gmail.com"
}


# In[25]:


people = {
    "first": ["Corey"],
    "last": ["Schafer"],
    "email": ["CoreyMScgafer@gmail.com"]
}


# In[26]:


people = {
    "first": ["Corey","Jane","John"],
    "last": ["Schafer","Doe","Doe"],
    "email": ["CoreyMScgafer@gmail.com","JaneDoe@email.com","JohnDoe@email.com"]
}


# In[27]:


dm = pd.DataFrame(people)


# In[57]:


dm


# In[60]:


dm.set_index('email', inplace=True)


# In[61]:


dm


# In[62]:


dm.index


# In[65]:


dm.loc['CoreyMScgafer@gmail.com', 'last']


# In[67]:


dm.iloc[0]


# In[70]:


dm.reset_index(inplace=True)


# In[72]:


dm


# In[101]:


filt = (dm['last'] == 'Schafer') | (dm['first'] == 'John')


# In[86]:


dm['email']


# In[89]:


dm[filt]


# In[103]:


dm.loc[~filt, 'email']


# In[121]:


dm.columns = ['first_name','last_name','email']


# In[155]:


dm.at[2, 'last'] = 'Doe'


# In[164]:



dm


# In[160]:


filt = (dm['email'] == 'JohnDoe@email.com')
dm.loc[filt,'last'] = 'Smith'


# In[208]:


dm


# In[199]:


dm['email'] = dm['email'].str.lower()


# In[165]:


dm['email'].apply(len)


# In[166]:


def update_email(email):
    return email.upper()


# In[168]:


dm['email'] = dm['email'].apply(update_email)


# In[170]:


dm['email'] = dm['email'].apply(lambda x:x.lower())


# In[172]:


dm['email'].apply(len)


# In[174]:


dm.apply(pd.Series.min)


# In[175]:


dm.apply(lambda x: x.min())


# In[177]:


dm.applymap(len)


# In[ ]:


dm.applymap(str.lower)


# In[179]:


dm['first'].map({'Corey':'Chris','Jane':'Mary'})


# In[181]:


dm['first'] = dm['first'].replace({'Corey':'Chris','Jane':'Mary'})


# In[188]:


dm['first']+ ' '+dm['last']


# In[190]:


dm['full_name'] = dm['first']+ ' '+dm['last']


# In[193]:


dm.drop(columns=['first','last'], inplace=True)


# In[196]:


dm['full_name'].str.split(' ',expand=True)


# In[207]:


dm[['first','last']] = dm['full_name'].str.split(' ',expand=True)


# In[210]:


dm.sort_values(by='last',ascending=False)


# In[211]:


dm.sort_values(by=['last','first'],ascending=False)


# In[212]:


dm.sort_values(by=['last','first'],ascending=[False, True])


# In[213]:


dm.sort_index()


# In[214]:


dm['last'].sort_values()


# In[ ]:





# In[ ]:





# In[203]:


dm.append({'first':'Tony'}, ignore_index=True)


# In[206]:


filt = dm['last'] == 'Doe'
dm.drop(index=dm[filt].index)


# In[129]:


dm.columns = dm.columns.str.replace(' ','_')


# In[134]:


dm.rename(columns={'first_name':'first', 'last_name':'last'}, inplace=True)


# In[31]:


dm.email


# In[34]:


dm[['last','email']]


# In[35]:


dm.columns


# In[43]:


dm.iloc[[0, 1], 2]


# In[47]:


dm.loc[[0, 1],['email', 'last']]


# In[48]:


df.columns


# In[50]:


df['Hobbyist'].value_counts()


# In[56]:


df.loc[0:2, 'Hobbyist':'ConvertedComp']


# In[78]:


schema_df


# In[81]:


schema_df.loc['NEWEdImpt', 'QuestionText']


# In[83]:


schema_df.sort_index(ascending=False)


# In[115]:


filt = df['LanguageWorkedWith'].str.contains('Python', na=False)


# In[119]:


df.loc[filt, 'LanguageWorkedWith']


# In[120]:


filt


# In[184]:


df.rename(columns={'ConvertedComp':'SalaryUSD'}, inplace=True)


# In[185]:


df['SalaryUSD']


# In[186]:


df['Hobbyist']


# In[187]:


df['Hobbyist'].map({'Yes':True,'No':False})


# In[221]:


df.sort_values(by=['Country','SalaryUSD'], ascending=[True,False], inplace=True)


# In[224]:


df[['Country', 'SalaryUSD']].head(300)


# In[225]:


df['SalaryUSD'].nlargest(10)


# In[228]:


df.nsmallest(10,'SalaryUSD')


# In[ ]:




