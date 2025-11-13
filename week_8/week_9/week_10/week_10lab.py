
'''#1 Create a Product class
class Product:
    #This will run the first as we create the class
    
    #private class variables 
    name = ''
    price = ''
    def __init__(self, input_name, input_price):
        self.name = input_name
        self.price = input_price
        self.quantity = 0 

    #Get Method
    def get_price(self):
        return self.price
    #Set Method
    def set_price(self, value):
        if value > 0:
            self.price = value
    #Get Method 
    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'the product is {self.name} and priced at {self.price} we have {self.quantity}'
    
appleiphone = Product('Iphone17promax', 1499)
mouse = Product('amazon mouse', 5)
computer = Product('Dell Computer', 1200)

print(appleiphone)
print(mouse)
print(computer)

#2 Create a Book Class 

class Book:
    def __init__(self, title, author, pageNum):
        self.title = title
        self.author = author 
        self.pageNum = pageNum
    
    
    def __str__(self):
        return f'the Book is {self.title} and the author is {self.author} we have {self.pageNum}'
    
lord_of_the_rings = Book('lord of the rings', 'John Tolkien', 10)
'''


#6 Create a Student Class

class Student:
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def get_name(self):
        return self.name
    def set_name(self,value):
       self.name = value
    def get_major(self):
        return self.major
    def get_major(self, value):
        self.major = value
    def get_gpa(self):
        return self.gpa
    def set_gpa(self, value):
        if 0 <= value <=4.0:
            self.gpa = value
    def introduce(self):
        return f"hi im {self.name}. i'm studying {self.major} and my gpa is {self.gpa}"
   
    def study_for_exam(self):
        if self.gpa <= 4.0:
            self.gpa += 0.2 
    
Will = Student('Will', 'CIT', 3.5)
Will.study_for_exam()
print(Will.introduce())

