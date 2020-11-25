#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter


# In[2]:


mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]


# In[3]:


Counter(mylist)


# In[4]:


mylist = ['a','a',10,10,10]


# In[5]:


Counter(mylist)


# In[6]:


Counter('aaaaabhjsdhabhjhsadbsda')


# In[7]:


sentence = "How many times does each word show up in this sentence with a word"


# In[8]:


Counter(sentence.lower().split())


# In[9]:


letters =' aaaaaaaabbbbbbcccccdddddddd'


# In[10]:


c = Counter(letters)


# In[11]:


c


# In[14]:


c.most_common(1)


# In[15]:


list(c)


# In[16]:


from collections import defaultdict


# In[17]:


d = {'a':10}


# In[18]:


d['a']


# In[19]:


d = defaultdict(lambda: 0)


# In[20]:


d['correct'] = 100


# In[21]:


d['WRONG KEY!']


# In[22]:


d


# In[23]:


mytuple = (10,20,30)


# In[24]:


from collections import namedtuple


# In[25]:


Dog = namedtuple('Dog',['age','breed','name'])


# In[26]:


sammy = Dog(age=5,breed='Husky',name='Sam')


# In[27]:


type(sammy)


# In[28]:


sammy


# In[33]:


import os


# In[34]:


os.getcwd()


# In[31]:


os.listdir('C:\\Users')


# In[32]:


import shutil


# In[39]:


shutil.move('practice.txt','C:\\Users\\DIKA')


# In[41]:


os.listdir('C:\\Users\\DIKA')


# In[42]:


import send2trash


# In[43]:


os.getcwd()


# In[44]:


import datetime


# In[50]:


mytime = datetime.time(13,20,1,20)


# In[51]:


mytime.minute


# In[52]:


mytime.hour


# In[53]:


print(mytime)


# In[54]:


today = datetime.date.today()


# In[55]:


print(today)


# In[56]:


today.year


# In[57]:


today.month


# In[58]:


today.day


# In[59]:


today.ctime()


# In[60]:


from datetime import datetime


# In[62]:


mydatetime = datetime(2021,10,3,14,20,1)


# In[65]:


print(mydatetime)


# In[64]:


mydatetime = mydatetime.replace(year=2020)


# In[66]:


from datetime import date


# In[67]:


date1 = date(2021,11,3)


# In[68]:


date2 = date(2020,11,3)


# In[70]:


result = date1 - date2


# In[71]:


type(result)


# In[72]:


result.days


# In[79]:


datetime1 = datetime(2021,11,3,22,0)


# In[80]:


datetime2 = datetime(2020,11,3,12,0)


# In[81]:


datetime1 - datetime2


# In[83]:


36000/60/60


# In[84]:


mydiff = datetime1 - datetime2


# In[88]:


mydiff.total_seconds()


# In[97]:


import math


# In[91]:


#help(math)


# In[102]:


value = 4.35


# In[103]:


math.floor(value)


# In[104]:


math.ceil(value)


# In[105]:


round(4.35)


# In[106]:


math.pi


# In[107]:


from math import pi


# In[108]:


pi


# In[110]:


math.inf


# In[111]:


math.log(math.e)


# In[112]:


math.log(100,10)


# In[115]:


math.sin(10)


# In[116]:


math.degrees(pi/2)


# In[117]:


math.radians(180)


# In[119]:


import random


# In[122]:


random.randint(0,100)


# In[125]:


random.seed(42)

random.randint(0,100)


# In[128]:


random.randint(0,100)


# In[129]:


random.randint(0,100)


# In[130]:


random.seed(42)

print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))


# In[131]:


mylist = list(range(0,21))


# In[136]:


random.choice(mylist)


# In[139]:


random.choices(population=mylist,k=10)


# In[140]:


random.sample(population=mylist,k=10)


# In[141]:


random.shuffle(mylist)


# In[142]:


mylist


# In[143]:


random.uniform(a=0,b=100)


# In[145]:


random.gauss(mu=0,sigma=1)


# In[147]:


x = [1,2,3]
y = 2
z = 3


# In[148]:


import pdb


# In[149]:


x = [1,2,3]
y = 2
z = 3

result_one = y + z

pdb.set_trace()

result_two = y + x


# In[ ]:




