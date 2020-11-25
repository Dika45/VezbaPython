#!/usr/bin/env python
# coding: utf-8

# In[8]:



name = 'John Doasdadsd'


# In[9]:


if len(name) > 20:
    print('Name "{}" is more than 20 chars long'.format(name))
    length_description = 'long'
elif len(name) > 15:
    print('Name "{}" is more than 15 chars long'.format(name))
    length_description = 'semi long'
elif len(name) > 10:
    print('Name "{}" is more than 10 chars long'.format(name))
    length_description = 'semi long'
elif len(name) == 8 or len(name) == 9 or len(name) == 10:
    print('Name "{}" is 8, 9 or 10 chars long'.format(name))
    length_description = 'semi short'
else:
    print('Name "{}" is a short name'.format(name))
    length_description = 'short'


# In[24]:



def stripped_reversed_lowercase(original):
    # Set a breakpoint here and start debugging
    stripped = original.strip()
    reve = ' '.join(reversed(stripped))
    return reve


# In[25]:


original = 'Original String'
result = stripped_reversed_lowercase(original)


# In[26]:


result == 'g n i r t s l a n i g i r o'


# In[27]:


print(result)


# In[28]:


my_dict = {'first_name': 'John','last_name':'Doe','hibbies':['Python','gym'],
           'age':82}


# In[37]:


print(my_dict)


# In[30]:


first_name = 'John'
last_name = 'Doe'
favorite_hobby = 'Python'
sports_hobby = 'gym'
age = 82


# In[36]:


my_dict = {'name':first_name+' '+last_name,'age':age,
          'hobbies':[favorite_hobby,sports_hobby]}


# In[45]:


dict1 = dict(key1='This is not that hard', key2='Python is still cool')
dict2 = {'key1': 123, 'special_key': 'secret'}
# This is also a away to initialize a dict (list of tuples) 
dict3 = dict([('key2', 456), ('keyX', 'X')])


# In[48]:


my_dict = {dict1["key1"],dict1["key2"],dict2["key1"],dict2["special_key"],
          dict3["key2"],dict3['keyX']}


# In[49]:


print(my_dict)


# In[50]:


words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
upper_case_words = []


# In[52]:


for nes in words:
    if nes.isupper():
        upper_case_words.append(nes)


# In[53]:


print(upper_case_words)


# In[65]:


magic_dict = dict(val1=44, val2='secret value', val3=55.0, val4=1)


# In[69]:


sum_of_values = 0
for key, value in magic_dict.items():
    if isinstance(value, int) or isinstance(value, float):
         sum_of_values += value
    
print(sum_of_values)
    


# In[70]:


numbers = [1, 3, 4, 6, 81, 80, 100, 95]


# In[71]:


my_list = []


# In[76]:


for nes in numbers:
    if nes%5 == 0 and nes%2 == 0:
        my_list.append('five even')
    elif nes%5 == 0 and nes%2 == 1:
        my_list.append('five odd')
    elif nes%2 == 0:
        my_list.append('even')
    elif nes%2 == 1:
        my_list.append('odd')


# In[77]:


print(my_list)


# In[80]:



def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# In[84]:


count_even_numbers([-2, 2, -10, 8])


# In[85]:


WANTED_PEOPLE = ['John Doe', 'Clint Eastwood', 'Chuck Norris']


# In[86]:


def find_wanted_people(lista):
    nova = []
    for n in lista:
        if n in WANTED_PEOPLE:
            nova.append(n)
    return nova


# In[87]:



people_to_check1 = ['Donald Duck', 'Clint Eastwood', 'John Doe', 'Barack Obama']


# In[88]:


wanted1 = find_wanted_people(people_to_check1)


# In[96]:


print(wanted1)


# In[90]:


'John Doe' in wanted1


# In[92]:


'Clint Eastwd'in wanted1


# In[93]:


people_to_check2 = ['Donald Duck', 'Mickey Mouse', 'Zorro', 'Superman', 'Robin Hood']


# In[94]:


wanted2 = find_wanted_people(people_to_check2)


# In[95]:


wanted2 == []


# In[98]:


def average_length_of_words(stringic):
    count = 0
    
    for letter in stringic:
        if letter != ' ':
            count += 1
        else:
            ukupno += count
    


# In[99]:


# Let's create an empty list
my_list = []

# Let's add some values
my_list.append('Python')
my_list.append('is ok')
my_list.append('sometimes')

# Let's remove 'sometimes'
my_list.remove('sometimes')

# Let's change the second item
my_list[1] = 'is neat'


# In[100]:


my_list


# In[101]:


original = ['I', 'am', 'learning', 'hacking', 'in']


# In[102]:


modified = list(original)


# In[104]:


modified.pop()


# In[107]:


modified.append('Python')


# In[108]:


original


# In[109]:


modified


# In[110]:



list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]


# In[111]:


my_list = list1+list2+list3


# In[114]:


my_list.sort()


# In[117]:


my_list.reverse()


# In[118]:


my_list


# In[119]:


a = 2
b = 3
c = 2


# In[120]:


result = 6*a**3-(8*b**2)/(4*c)+11


# In[121]:


print(result)


# In[202]:



VOWELS = ['a', 'e', 'i', 'o', 'u']


# In[204]:


def super_vowels(stringic):
    modif = stringic.split()
    novi = ''
    for n in modif:
        for letter in n:
            if letter in VOWELS:
                letter.upper()
    for n in modif:
        novi = novi+' '+n
    return novi
        


# In[205]:


super_vowels('hi wassup!')


# In[206]:


print(sta)


# In[134]:


ase = 'sdadssad adsda dasda'


# In[135]:


ase.upper()


# In[139]:


ROCK = 1
PAPER = 2
SCISSORS = 3

PLAYER_WINS = 'Player wins!! Woop woop!'
COMPUTER_WINS = 'Robocop wins :-('
TIE = "It's a tie!"


# In[140]:


ROCK = 1
PAPER = 2
SCISSORS = 3

PLAYER_WINS = 'Player wins!! Woop woop!'
COMPUTER_WINS = 'Robocop wins :-('
TIE = "It's a tie!"


# In[141]:


import random


# In[234]:


def rock_paper_scissors(choice):
    comp = random.randint(1,3)
    print("Compjuter picks: {}".format(comp))
    if comp == choice:
        print(TIE)
    elif comp == ROCK:
        if choice == PAPER:
            print(PLAYER_WINS)
        elif choice == SCISSORS:
            print(COMPUTER_WINS)
    elif comp == PAPER:
        if choice == ROCK:
            print(COMPUTER_WINS)
        elif choice == SCISSORS:
            print(PLAYER_WINS)
    else:
        if choice == ROCK:
            print(PLAYER_WINS)
        elif choice == PAPER:
            print(COMPUTER_WINS)


# In[235]:


def play_rps():
    print('Welcome to play rock-paper-scissors')
    print('The options are:\nrock: 1\npaper: 2\nscissors: 3')

    result = TIE
    while result == TIE:
        player_choice = input('Give your choice\n')
        
        if not player_choice in ['1', '2', '3']:
            print('Invalid choice')
            continue
            
        result = rock_paper_scissors(int(player_choice))
        
if __name__ == '__main__':
    play_rps()


# In[162]:


original = ' Python strings are COOL! '
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.lower().strip()


# In[165]:


print(stripped_lower_cased)


# In[166]:


verb = 'is'
language = 'Python'
punctuation = '!'


# In[170]:


sentence = "Learning "+language+' '+verb+" fun "+punctuation


# In[171]:


print(sentence)


# In[174]:



print('sentence: {}'.format(sentence))


# In[175]:


my_string = 'Python is my favorite programming language!'


# In[176]:



my_modified_string = my_string.replace('is', 'will be')
print(my_modified_string)


# In[185]:


pandas = 'pandas'
numpy = 'numpy'
requests = 'requests'
cool_python_libs = ' '.join([pandas, numpy, requests])


# In[186]:


print('Some cool python loibraries: {}'.format(cool_python_libs))


# In[187]:


mixed_case = 'PyTHoN hackER'


# In[188]:


mixed_case.upper()


# In[189]:


mixed_case.lower()


# In[190]:


mixed_case.title()


# In[191]:


ugly_formatted = ' \n \t Some story to tell '
stripped = ugly_formatted.strip()

print('ugly: {}'.format(ugly_formatted))
print('stripped: {}'.format(ugly_formatted.strip()))


# In[195]:



sentence = 'three different words'
words = sentence.split()
print(words)


# In[196]:



ugly = ' tiTle of MY new Book\n\n'


# In[197]:


stripped = ugly.strip()


# In[198]:


print(stripped)


# In[199]:


stripped.lower()


# In[201]:


stripped.title()


# In[219]:


def average_length_of_words(stringic):
    count = 0
    con = 0
    prox = 0
    for let in stringic:
        if let == ' ':
            con += 1
        else:
            count += 1
        
    prox = round(count/(con+1),1)
    return prox


# In[216]:


average_length_of_words('only four lett erwo rdss')


# In[220]:


average_length_of_words('one two three')


# In[221]:


average_length_of_words('one two three four')


# In[222]:


average_length_of_words('')


# In[229]:


def get_playing_board(laka):
    
    bor = ''
    for n in range(laka):
        if n%2 == 0:
            print(' * * * * *')
        else:
            print('* * * * * ')


# In[231]:


get_playing_board(10)


# In[237]:



my_dict = {'a': 1, 'b': 2, 'c': 3}


# In[238]:


if 'g' in my_dict:
    value = my_dict['g']
else:
    value = 'some default value'
print(value)


# In[239]:


my_dict


# In[241]:


value = my_dict.get('b', 'some default value')
print(value)


# In[242]:


my_dict = {'a': 1, 'b': 2, 'c': 3}

key = 'g'
if key in my_dict:
    value = my_dict[key]
else:
    value = 'some default value'
    my_dict[key] = value
    
print(value)
print(my_dict)


# In[246]:


my_dict = {'a': 1, 'b': 2, 'c': 3}

key = 'g'
value = my_dict.setdefault(key, 'some default value')

print(value)
print(my_dict)


# In[249]:


my_dict


# In[248]:


my_dict.setdefault('s',5)


# In[250]:



numbers = (1, 5, 10)


# In[251]:



squares = {}
for num in numbers:
    squares[num] = num**2
print(squares)


# In[252]:


squares = {num: num**2 for num in numbers}
print(squares)


# In[256]:


keys = ('a', 'b', 'c')
values = [True, 100, 'John Doe']


# In[259]:


my_dict = {}
for idx, key in enumerate(keys):
    my_dict[key] = values[idx]
print(my_dict)


# In[ ]:




