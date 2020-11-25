#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


f = open('fileone.txt','w+')
f.write('ONE FILE')
f.close()


# In[3]:


f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()


# In[4]:


import zipfile


# In[5]:


comp_file = zipfile.ZipFile('comp_file.zip','w')


# In[6]:


comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)


# In[7]:


comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)


# In[8]:


comp_file.close()


# In[9]:


zip_obj = zipfile.ZipFile('comp_file.zip','r')


# In[11]:


zip_obj.extractall('extracted_content')


# In[13]:


pwd


# In[47]:


import shutil


# In[16]:


dir_to_zip = 'C:\\Users\\DIKA\\DikaPhyton\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content'


# In[17]:


output_filename = 'example'


# In[18]:


shutil.make_archive(output_filename,'zip',dir_to_zip)


# In[36]:


os.getcwd()


# In[20]:


shutil.unpack_archive('unzip_me_for_instructions.zip','final_unzip','zip')


# In[46]:


import os


# In[30]:


os.listdir("C:\\Users\\DIKA\\DikaPhyton\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\final_unzip\\extracted_content\\One")


# In[45]:


import re


# In[33]:


pattern =r'\d{3}-\d{3}-\d{4}'


# In[49]:


def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''


# In[50]:


results = []


# In[51]:


for folder,sub_foleders,files in os.walk(os.getcwd()+'\\final_unzip\\extracted_content'):
    
    for f in files:
        full_path = folder+'\\'+f
        
        
        results.append(search(full_path))
    


# In[52]:


for r in results:
    if r != '':
        print(r.group())


# In[54]:


nes = 'Anthopomorphism'


# In[57]:


def myfunc(nes):
    modif = ''
    for num in range(len(nes)):
        if num%2 == 0:
            modif += nes[num].lower()
        else:
            modif += nes[num].upper()
    return modif


# In[60]:


myfunc(nes)


# In[97]:


def sum_of_list(values):
    suma = 0
    for val in values:
        try:
            numeric_val = float(val)
        except:
            continue
        suma += numeric_val
    return suma


# In[98]:


list1 = [1, 2, 3]
list2 = ['1', 2.5, '3.0']
list3 = ['', '1']
list4 = []
list5 = ['John', 'Doe', 'was', 'here']
nasty_list = [KeyError(), [], dict()]


# In[99]:


sum_of_list(list1)


# In[100]:


sum_of_list(list2)


# In[101]:


sum_of_list(list3)


# In[102]:


sum_of_list(list4)


# In[103]:


sum_of_list(list5)


# In[119]:


string = 'sdasdadsda'


# In[129]:


def verify_short_string(string):
    if len(string)>10:
        raise NameError('Ovaj je bas smarac')
  
    


# In[130]:


len(string)


# In[133]:


verify_short_string('this is long')


# In[134]:


TooLongString = 'erorija'


# In[135]:


try:
    verify_short_string('this is long')
except TooLongString as e:
    # This is ok
    pass
else:
    # This means that there was no exception
    assert False


# In[136]:


stri = 'baka'


# In[138]:


modif = ''


# In[141]:


for s in range(len(stri)):
    if s ==2:
        modif += stri[s].upper()
    else:
        modif += stri[s]


# In[142]:


modif


# In[143]:


d = {'key1':1,'key2':2,'key3':3}


# In[144]:


del d['key3']


# In[245]:


import math


# In[254]:


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}


# In[147]:


inventory['pocket'] = ['seashell','strange berry','lint']


# In[256]:


inventory


# In[154]:


inventory['backpack'].sort()


# In[156]:


inventory['backpack'].remove('dagger')


# In[255]:


inventory['gold'] = inventory['gold']+50


# In[163]:


prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}


# In[174]:


for key,value in prices.items():
    print(key)
    print('price: '+str(value))
    print('stock: '+str(stock[key]))
        


# In[168]:


total = 0


# In[169]:


stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}


# In[259]:


for key in prices.keys():
    ved = prices[key]*stock[key]
    print(key+'vednost: {}'.format(ved))
    total += ved
print('Total je: {}'.format(total))


# In[199]:


groceries = ["banana","orange","apple"]


# In[200]:


def compute_bill(food):
    total = 0
    
    for food in food:
        for key in prices:
            if key == food:
                if stock[key] > 0:
                    total += prices[key]
                    prices[key] = prices[key]-1
    return total


# In[202]:


compute_bill(groceries)


# In[270]:


students = [lloyd,alice,tyler]


# In[267]:


lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


# In[271]:


for student in students:
        print(student['name'])
        print(student['homework'])
        print(student['quizzes'])
        print(student['tests'])


# In[272]:


def func_avra(listic):
    total = sum(listic)
    total = float(total)
    divi = total/(len(listic))
    return divi


# In[273]:


print(func_avra([1,2,5,3,5,6,8]))


# In[274]:


def get_avrage(student):
    homework = func_avra(student['homework'])
    quizzes = func_avra(student['quizzes'])
    tests = func_avra(student['tests'])
 
    final = 0.1*homework + 0.3*quizzes + 0.6*tests
    return final


# In[275]:


get_avrage(lloyd)


# In[276]:


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif socre >= 70:
        return "C"
    elif socre >= 60:
        return "D"
    else:
        return "F"


# In[277]:


get_letter_grade(get_avrage(lloyd))


# In[278]:


likala = [lloyd,tyler,alice]


# In[248]:


def get_class_average(students):
    results = []
    count = 0
    ukupno = 0
    
    for item in students:
        results.append(get_avrage(item))
        count += 1
    for res in results:
        ukupno += res
    
    return ukupno/count


# In[250]:


print(get_class_average(likala))


# In[279]:


import pandas


# In[ ]:




