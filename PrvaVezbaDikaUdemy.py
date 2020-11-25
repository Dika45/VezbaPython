#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello')


# In[2]:


print('new')


# here you can write notes

# In[3]:


print('new')


# In[4]:


2+1


# In[5]:


2-1


# In[6]:


2*2


# In[7]:


3/2


# In[8]:


7 %4


# In[9]:


50% 5


# In[10]:


23 % 2


# In[11]:


a = 5
a = 10


# In[14]:


a= a + a


# In[15]:


print(a)


# In[16]:


type(a)


# In[18]:


a = 31.1
type(a)


# In[21]:


my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print(my_taxes)


# In[22]:


'hello'


# In[23]:


" I'm going on a run"


# In[24]:


print("hello")


# In[25]:


print('g\n g')


# In[26]:


len('majkata na frikata baluzis')


# In[27]:


mystring = "Hello World"
mystring


# In[28]:


mystring[0]


# In[29]:


mystring[8]


# In[30]:


mystring[-2]


# In[33]:


mystring = 'abcdefghijk'


# In[34]:


mystring[2:]


# In[35]:


mystring[:3]


# In[36]:


mystring[3:-5]


# In[37]:


mystring[1:3]


# In[38]:


mystring[::-1]


# In[46]:


name = "Sam"
last_letters = name[1:]
last_letters


# In[47]:


'P' + last_letters


# In[44]:


x = 'Hello World'


# In[59]:


x = 'Hello World '
x = x + "it is beautiful outside"


# In[60]:


x


# In[63]:


x= 'Hello World'


# In[64]:


x.join("bala")


# In[65]:


x.upper()


# In[66]:


x.split()


# In[68]:


x = 'Hi this is a string'
x.split("i")


# In[69]:


print('hello')


# In[70]:


print('This is a string {}.'.format('INSERTED'))


# In[72]:


print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))


# In[73]:


print('The {q} {b} {f}'.format(f='fox',b='brown', q='quick'))


# In[74]:


result = 100/777


# In[75]:


result


# In[85]:


print("The result was {r:1.2f}".format(r=result))


# In[84]:


result = 104.12845


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[86]:


name="Jose"


# In[91]:


print(f'Hello, his name is {name}')


# In[92]:


name = "Sam"
age = 3


# In[93]:


print(f'{name} is {age} years old.')


# In[94]:


my_list = [1,2,3]


# In[95]:


my_list = ['STRING',100,23.2]


# In[96]:


len(my_list)


# In[97]:


mylist = ['one','two','three']


# In[99]:


mylist[1:]


# In[100]:


another_list = ['four','five']


# In[101]:


mylist + another_list


# In[102]:


mylist


# In[103]:


another_list


# In[104]:


new_list = mylist + another_list


# In[105]:


new_list


# In[106]:


new_list[0] = 'ONE ALL CAPS'


# In[107]:


new_list


# In[108]:


new_list.append('six')


# In[109]:


new_list


# In[110]:


new_list.append('seven')


# In[111]:


new_list


# In[112]:


new_list.pop()


# In[113]:


popped_item = new_list.pop()


# In[114]:


popped_item


# In[115]:


new_list


# In[116]:


new_list.pop(0)


# In[117]:


new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]


# In[118]:


new_list.sort()


# In[119]:


new_list


# In[120]:


new_list.sort()
my_sorted_list = new_list


# In[122]:


my_sorted_list


# In[123]:


num_list.sort()


# In[124]:


num_list


# In[125]:


num_list.reverse()


# In[126]:


num_list


# In[129]:


my_dict ={'key1':'value1','key2':'value2'}


# In[130]:


my_dict


# In[131]:


my_dict['key1']


# In[132]:


prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}


# In[133]:


prices_lookup['apple']


# In[136]:


d = {'k1':123, 'k2':[0,1,2],'k3':{'insidekey':100}}


# In[137]:


d['k2']


# In[138]:


d['k2'][2]


# In[143]:


d['k3']['insidekey']


# In[145]:


d = {'key1': ['a','b','c']}


# In[146]:


d


# In[147]:


mylist = d['key1']


# In[148]:


mylist


# In[149]:


letter = mylist[2]
letter


# In[152]:


d['key1'][2].upper()


# In[153]:


d = {'k1':100,'k2':200}


# In[154]:


d


# In[155]:


d['k3'] =300


# In[156]:


d


# In[158]:


d['k1'] = 'NEW VALUE'


# In[ ]:





# In[159]:


d = {'k1':100,'k2':200, 'k3': 300}


# In[160]:


d.values()


# In[161]:


d.items()


# In[162]:


t = (1,2,3)


# In[163]:


mylist = [1,2,3]


# In[164]:


type(t)


# In[165]:


type(mylist)


# In[166]:


len(t)


# In[167]:


t


# In[168]:


t=('one',2)
t[0]


# In[169]:


t[-1]


# In[170]:


t = ('a','a','b')


# In[171]:


t.count('a')


# In[172]:


t.index('a')


# In[174]:


t.index('b')


# In[175]:


mylist


# In[177]:


t[0] = 'NEW'


# In[178]:


myset = set()


# In[179]:


myset


# In[181]:


myset.add(1)


# In[ ]:





# In[182]:


myset.add(2)


# In[183]:


myset


# In[184]:


myset.add(2)


# In[ ]:





# In[185]:


myset


# In[186]:


mylist = [1,1,1,1,23,2,3,12,1,2,2,2,]


# In[187]:


set(mylist)


# In[188]:


True


# In[189]:


False


# In[190]:


type(False)


# In[191]:


b = True


# In[192]:


type(b)


# In[193]:


1 > 2


# In[194]:


1 == 1


# In[195]:


b = None


# In[196]:


b


# In[197]:


type(b)


# In[198]:


set([1,1,2,3])


# In[202]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is a text file\nthis is the second line\nthis is the third line ')


# In[203]:


myfile = open('myfile.txt')


# In[204]:


myfile = open('woops_wrong.txt')


# In[205]:


pwd


# In[206]:


myfile = open('myfile.txt')


# In[207]:


myfile.read()


# In[208]:


myfile.read()


# In[209]:


myfile.seek(0)
myfile.read()


# In[211]:


myfile.seek(0)


# In[212]:


myfile.seek(0)


# In[213]:


myfile.read()


# In[214]:


myfile.seek(0)


# In[215]:


contents = myfile.read()


# In[216]:


contents


# In[217]:


myfile.seek(0)


# In[218]:


myfile.readlines()


# In[219]:


pwd


# In[220]:


myfile.close()


# In[221]:


with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()


# In[222]:


contents


# In[225]:


with open('myfile.txt',mode='a') as myfile:
    contents = myfile.read()


# In[224]:


contents


# In[226]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')


# In[228]:


with open('my_new_file.txt',mode = 'r') as f:
    print(f.read())


# In[236]:


with open('my_new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')


# In[237]:


with open('my_new_file.txt',mode = 'r') as f:
    print(f.read())


# In[238]:


with open('dasdasdsadadsa.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')


# In[239]:


with open('dasdasdsadadsa.txt', mode='r') as f:
    print(f.read())


# In[ ]:




