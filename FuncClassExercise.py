#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shut_down(s):
    if s == 'yes':
        return "Shutting down"
    elif s == 'no':
        return "Shutdown aborted"
    else:
        return "Sorry"


# In[2]:


import math


# In[4]:


num = 13689


# In[5]:


math.sqrt(num)


# In[6]:


def distance_from_zero(nes):
    if type(nes) == int or type(nes) == float:
        return abs(nes)
    else:
        return "Nope"


# In[7]:


distance_from_zero(-5.6)


# In[35]:


def computepay(hours,rate):
    pay = 0
    if hours > 40:
        pay += (40*rate)
        pay += (hours-40)*rate*1.5
    else:
        pay = hours*rate
    print("Enter Hours: {}".format(hours))
    print("Enter Rate: {}".format(rate))
    print("Pay: {}".format(pay))


# In[37]:


computepay(50,10)


# In[12]:


def hotel_cost(nights):
    return nights*140


# In[16]:


def plane_ride_cost(city):
    for key in citys.keys():
        if key == city:
            return citys[key]


# In[15]:


citys = {"Charlotte": 183,
"Tampa": 220,
"Pittsburgh": 222,
"Los Angeles": 475}


# In[17]:


plane_ride_cost("Tampa")


# In[21]:


def renatal_car_cost(days):
    calc = 0
    if days < 3:
        calc = days*40
        return calc
    elif days >= 3 and days < 7:
        calc = (days*40)-20
        return calc
    elif days >= 7:
        calc =(days*40)-50
        return calc


# In[24]:


renatal_car_cost(5)


# In[27]:


def trip_cost(city,days,spending_money):
    hotel = hotel_cost(days)
    rentcar = renatal_car_cost(days)
    plane = plane_ride_cost(city)
    
    return hotel+rentcar+plane+spending_money


# In[28]:


trip_cost("Pittsburgh",10,600)


# In[29]:


def cube(number):
    return number**3


# In[31]:


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


# In[34]:


by_three(3)


# In[38]:


class Triangle():
    
    number_of_sides = 3
    
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    def check_angles(self):
        suma = self.angle1+self.angle2+self.angle3
        if suma == 180:
            return True
        else:
            return False
        


# In[39]:


my_triangle = Triangle(90,30,60)


# In[40]:


print(my_triangle.number_of_sides)


# In[41]:


my_triangle.check_angles()


# In[49]:


class Songs():
    
    def __init__(self,lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for n in self.lyrics:
            print("{}\n".format(n))


# In[50]:


happy_bday = Songs(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])


# In[51]:


happy_bday.sing_me_a_song()


# In[61]:


class Lunch():
    
    def __init__(self,menu):
        self.menu = menu
        
    def menu_price(self):
        if self.menu == 'menu 1':
            print('Your choice: {} Price 12.00'.format(self.menu))
        elif self.menu == 'menu 2':
            print('Your choice: {} Price 13.40'.format(self.menu))
        else:
            print('Error in menu')


# In[62]:


Paul = Lunch('menu 1')


# In[63]:


Paul.menu_price()


# In[77]:


class Point3D():
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "(%d, %d, %d)"%(self.x,self.y,self.z)


# In[78]:


my_point = Point3D(1,2,3)


# In[79]:


print(my_point)


# In[80]:


hex(12)


# In[ ]:




