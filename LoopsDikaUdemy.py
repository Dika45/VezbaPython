#!/usr/bin/env python
# coding: utf-8

# In[21]:





# In[14]:



    


# In[1]:


2 == 2


# In[2]:


2 == 1


# In[3]:


'hello' == 'bye'


# In[4]:


'Bye' == 'bye'


# In[5]:


'2' == 2


# In[7]:


2.0 == 2


# In[8]:


3 != 3


# In[9]:


4 != 5


# In[10]:


2 > 1


# In[11]:


1 > 2


# In[12]:


1 < 2


# In[13]:


2 < 5


# In[14]:


2 >= 2


# In[15]:


4 <= 1


# In[16]:


1 < 2 < 3


# In[18]:


1 < 2 and 2 > 3


# In[19]:


'h' == 'h' and 2 == 2


# In[21]:


1 == 3 or 2 == 2


# In[22]:


not(1 == 1)


# In[24]:


not 400 > 500


# In[31]:


hungry = False

if hungry:
    print('FEED ME!')
else:
    print('Im not hungry')


# In[34]:


loc = 'dasda'

if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool!")
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print("I do not know much.")


# In[37]:


name = 'Jose'

if name == 'Frankie':
    print("Hello Frankie!")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("Want is your name")


# In[38]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[40]:


for jelly in mylist:
    print(jelly)


# In[42]:


for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')


# In[46]:


list_sum = 0

for num in mylist:
    list_sum += num
    
print(list_sum)


# In[49]:


mystring = 'Hello World'

for _ in mystring:
    print('Cool!')


# In[50]:


tup = (1,2,3)

for item in tup:
    print(item)


# In[51]:


mylist = [(1,2),(3,4),(5,6),(7,8)]


# In[52]:


len(mylist)


# In[55]:


for a,b in mylist:
    print(a)
    print(b)


# In[56]:


mylist = [(1,2,3),(5,6,7),(8,9,10)]


# In[59]:


for a,b,c in mylist:
    print(b)


# In[62]:


d = {'k1':1,'k2':2,'k3':3}

for key , value in d.items():
    print(value)


# In[1]:


x = 0

while x < 5:
    print(f'the current value of x is {x}')
    x += 1


# In[3]:


x = 0

while x < 5:
    print(f'the current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THEN 5")


# In[5]:


x = [1,2,3]

for item in x:
    pass

print('end of my script')


# In[8]:


mystring = 'Sammy'


# In[14]:


for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
    


# In[13]:


x=0

while  x < 5:
    
    if x == 2:
        break
    print(x)
    x += 1


# In[15]:


mylist = [1,2,3]


# In[19]:


for num in range(0,11,2):
    print(num)


# In[20]:


list(range(0,11,2))


# In[27]:



word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    
  


# In[31]:


mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]


# In[35]:


for item in zip(mylist1, mylist2, mylist3):
    print(item)


# In[33]:


list(zip(mylist1,mylist2,mylist3))


# In[36]:


'x' in ['x',2,3]


# In[38]:


'a' in 'aworld'


# In[39]:


'mykey' in {'mykey':345}


# In[40]:


d = {'mykey':345}

345 in d.values()


# In[41]:


mylist = [10,20,30,40,100]


# In[43]:


min(mylist)


# In[44]:


max(mylist)


# In[45]:


from random import shuffle


# In[46]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[49]:


shuffle(mylist)


# In[50]:


mylist


# In[51]:


from random import randint


# In[54]:


randint(0,100)


# In[55]:


mynum = randint(0,10)


# In[56]:


mynum


# In[62]:


result = int(input('Enter a number here: '))


# In[59]:


type(result)


# In[60]:


float(result)


# In[61]:


int(result)


# In[72]:


mystring = 'hello'


# In[73]:


mylist = []

for letter in mystring:
    mylist.append(letter)
    


# In[74]:


mylist


# In[75]:


mylist = [letter for letter in mystring]


# In[76]:


mylist


# In[77]:


mylist = [x for x in 'word']


# In[80]:


mylist


# In[86]:


mylist = [num**2 for num in range(0,11)]


# In[87]:


mylist


# In[90]:


mylist = [x**2 for x in range(0,11) if x%2==0]


# In[91]:


mylist


# In[92]:


celcius = [0,10,20,34.5]

far = [((9/5)*temp + 32) for temp in celcius]


# In[93]:


far


# In[96]:


far = []

for temp in celcius:
    far.append(( (9/5)*temp + 32))


# In[97]:


far


# In[98]:


results = [x if x%2==0 else 'ODD' for x in range(0,11)]


# In[100]:


results


# In[104]:


mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)


# In[105]:


mylist


# In[106]:


mylisy = [x*y for x in [2,4,6] for y in [1,10,1000]]


# In[107]:


mylisy


# In[ ]:




