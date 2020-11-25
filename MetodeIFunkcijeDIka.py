#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[2]:


mylist.append(4)


# In[3]:


mylist


# In[4]:


mylist.pop()


# In[5]:


mylist


# In[9]:


def say_hello():
    print("hello")
    print('are')
    print('you')


# In[10]:


say_hello()


# In[13]:


def say_hello(name='Default'):
    print(f'Hello {name}')


# In[14]:


say_hello()


# In[15]:


def add_num(num1,num2):
    return num1+num2


# In[17]:


result = add_num(10,20)


# In[18]:


result


# In[19]:


def print_result(a,b):
    print(a+b)
    


# In[20]:


def return_result(a,b):
    return a+b


# In[21]:


print_result(10,20)


# In[22]:


result = return_result(10,20)


# In[23]:


result


# In[24]:


def myfunc(a,b):
    print(a+b)
    return a+b


# In[25]:


result = myfunc(10,20)


# In[26]:


def sum_numbers(num1,num2):
    return num1+num2


# In[27]:


sum_numbers(10,20)


# In[28]:


2 % 2


# In[31]:


def even_check(number):
    return number % 2 == 0


# In[32]:


even_check(20)


# In[43]:


def check_even_list(num_list):
    
    even_numbers = []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
        
    return even_numbers
        

    


# In[38]:


check_even_list([1,3,5])


# In[39]:


check_even_list([1,4,5])


# In[36]:


check_even_list([1,1,1,4])


# In[44]:


check_even_list([1,2,3,4,5])


# In[45]:


stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]


# In[46]:


for item in stock_prices:
    print(item)


# In[47]:


for ticker,price in stock_prices:
    print(price+(0.1*price))


# In[52]:


work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]


# In[49]:


def employee_check(work_hours):
    
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    
    return(employee_of_month,current_max)


# In[55]:


result = employee_check(work_hours)


# In[57]:


name,hours = employee_check(work_hours)


# In[58]:


name


# In[59]:


hours


# In[63]:


example = [1,2,3,4,5,6,7]


# In[62]:


from random import shuffle


# In[64]:


shuffle(example)


# In[65]:


example


# In[66]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[71]:


result = shuffle_list(example)


# In[72]:


result


# In[73]:


mylist = [' ','O',' ']


# In[74]:


shuffle_list(mylist)


# In[75]:


def player_guess():
    
    guess =''
    
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2")
    
    return int(guess)


# In[76]:


player_guess()


# In[77]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# In[81]:


#INITIAL LIST
mylist = [' ','O',' ']

#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)


# In[85]:


def myfunc(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum of a and b
    
    return sum((a,b)) * 0.05


# In[86]:


myfunc(40,60,100,100,3)


# In[87]:


def myfunc(*args):
    return sum(args) * 0.05


# In[88]:


myfunc(40,60)


# In[91]:


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


# In[92]:


myfunc(fruit='apple', veggie='lettuce')


# In[95]:


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))


# In[96]:


myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')


# In[97]:


def square(num):
    return num**2


# In[98]:


my_nums = [1,2,3,4,5]


# In[100]:


for item in map(square, my_nums):
    print(item)


# In[101]:


list(map(square, my_nums))


# In[103]:


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


# In[104]:


names = ['Andy','Eve','Sally']


# In[105]:


list(map(splicer,names))


# In[106]:


def check_even(num):
    return num%2 == 0


# In[107]:


mynums = [1,2,3,4,5,6]


# In[108]:


list(filter(check_even,mynums))


# In[110]:


for n in filter(check_even,mynums):
    print(n)


# In[115]:


square = lambda num: num **2


# In[117]:


square(5)


# In[118]:


list(map(lambda num:num**2,mynums))


# In[120]:


list(filter(lambda num: num%2 == 0,mynums))


# In[122]:


list(map(lambda name:name[::-1],names))


# In[123]:


x = 25

def printer():
    x = 50
    return x


# In[124]:


print(x)


# In[125]:


print(printer())


# In[127]:


#lambda num:num**2


# In[133]:


# GLOBAL
#name = 'THIS IS A GLOBAL STRING'

def greet():
    
    # ENCLOSING
    #name = 'Sammy'
    
    def hello():
        #LOCAL
        #name = 'IM A LOCAL'
        print('Hello '+name)
        
    hello()


# In[134]:


greet()


# In[151]:


x = 50

def func(x):

    print(f'X is {x}')
    
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')
    return x


# In[153]:


x = func(x)


# In[154]:


print(x)


# In[ ]:





# In[ ]:




