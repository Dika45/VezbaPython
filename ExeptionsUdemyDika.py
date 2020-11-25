#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(n1,n2):
    print(n1+n2)


# In[2]:


add(10,20)


# In[3]:


number1 = 10


# In[4]:


number2 = input("davaj broj: ")


# In[5]:


add(number1,number2)
print("Something happend!")


# In[7]:


try:
    result = 10 + 10
except:
    print("Hey it looks like yournt adding correctly!")
else:
    print("Add went well!")
    print(result)
    


# In[ ]:





# In[11]:


try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except:
    print("All other exept")
finally:
    print("I always run")


# In[14]:


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Woops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")


# In[17]:


ask_for_int()


# In[ ]:





# In[ ]:




