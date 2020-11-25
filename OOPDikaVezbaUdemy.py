#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[2]:


myset = set()


# In[3]:


type(myset)


# In[4]:


type(mylist)


# In[40]:


class Dog():
    
    species = 'mammal'
    
    def __init__(self,breed,name):
        
        self.breed = breed
        self.name = name

    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))


# In[6]:


my_sample = Sample()


# In[7]:


type(my_sample)


# In[11]:


my_dog = Dog(breed='Lab')


# In[12]:


type(my_dog)


# In[13]:


my_dog.breed


# In[41]:


my_dog = Dog('Lab','Frankie')


# In[31]:


my_dog.name


# In[42]:


my_dog.bark(10)


# In[33]:


my_dog.species


# In[ ]:





# In[ ]:





# In[ ]:





# In[63]:


class Circle():
    
    pi = 3.14
    
    def __init__(self,radius=1):
        
        self.radius = radius
        self.area = radius*radius*Circle.pi
        
    def get_circumference(self):
        return self.radius * Circle.pi * 2


# In[64]:


my_circle = Circle(30)


# In[65]:


my_circle.pi


# In[66]:


my_circle.radius


# In[67]:


my_circle.area


# In[71]:


class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")


# In[81]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
    def who_am_i(self):
        print("I am a dog")
        
    def bark(self):
        print("WOOF!")
    


# In[82]:


mydog = Dog()


# In[84]:


mydog.who_am_i()


# In[88]:


class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof!"


# In[89]:


class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow!"


# In[87]:


niko = Dog("niko")
felix = Cat("felix")


# In[90]:


print(niko.speak())


# In[91]:


print(felix.speak())


# In[93]:


for pet in [niko,felix]:
    
    print(type(pet))
    print(pet.speak())


# In[94]:


def pet_speak(pet):
    print(pet.speak())


# In[95]:


pet_speak(niko)


# In[96]:


pet_speak(felix)


# In[97]:


class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[100]:


class Dog(Animal):
    
    def speak(self):
        return self.name+ " says woof!"


# In[101]:


class Cat(Animal):
    
    def speak(self):
        return self.name+ " says meow!"


# In[102]:


fido = Dog("Fido")


# In[103]:


isis = Cat("Isis")


# In[104]:


print(fido.speak())


# In[105]:


print(isis.speak())


# In[106]:


mylist = [1,2,3]


# In[107]:


len(mylist)


# In[108]:


class Sample():
    pass


# In[109]:


mysample = Sample()


# In[127]:


class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")


# In[128]:


b = Book('Python rocks','Jose',200)


# In[129]:


print(b)


# In[126]:


str(b)


# In[122]:


len(b)


# In[130]:


del b


# In[ ]:




