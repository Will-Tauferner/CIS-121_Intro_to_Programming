'''
dog1_name = 'spot'
dog1_age = 
dog1_weight = 
dog1_breed = 
dog1_size = 
'''
'''
class Classname:
    def method1():
        #block of code
    def method2():
        #block of code
'''
#The first method that many classes have is called a constructor, which defines the way the object is created
#The constructor can create instance variable to hold the values of an instance of the object class.  

#In Python, the constructor is called __init__().

#ALl methods (in python) require one special parameter (the first parameter) which refers to the object that is being created.

#lets see an example of a planet class that has a 
#1. name
#2. radius
#3. mass
#4. distance

class Planet:
    def __init__(self, _name):
        self.name = _nameplanet1 = 
planet1 = Planet('x25')


#Lets see an example of a dog class that has a 
#1name
#2 age 
#3 Breed 

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    print(__init__('banzai',3,'shiba'))
