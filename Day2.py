# OOPS

# 1. What is OOPS 
# OOPS also known as Object Oriented Programming is an approach by whuch we can sove a problem by creating objects

# 2. Class and Object
# Class is a blueprint for creating objects while objects are an instance of a class which has its own unique set of attribute values.

class MyClass:
    pass 

obj = MyClass()

# 3. Data members in a class
# a. Instance Variables
# The attributes which are specific to each instance of a class are known as instance variables. They can have different values for different instances of the same class

class MyClass:
    def increment(self):
        if not hasattr(self, 'instance_var'):  
            self.instance_var = 0  
        self.instance_var += 1  
        return self.instance_var  

obj = MyClass()  

print(obj.increment())  
print(obj.increment())

# b. Class variables
# Variables that are shared among all instances of a class are known as class variables. Class variables are common to all objects of the same class.

class MyClass:
    class_var = 0  
    def increment(self):  
        MyClass.class_var += 1  

obj1 = MyClass()  
obj2 = MyClass()  

print(MyClass.class_var)  
obj1.increment()  
print(MyClass.class_var)  
obj2.increment()
print(MyClass.class_var)

# 4. Methods in class:

# a. Normal method
# The most common type of methods in Python classes.These methods have access to the instance data through the self parameter, which refers to the current instance of the class.

class MyClass:
    def my_method(self):
        print("This is a normal method.")

obj = MyClass()
obj.my_method() 

# b. Class Method
# Methods that are bound to the class itself, not to a specific instance. 
class MyClass:
    class_var = 0

    def increment(self):  
        MyClass.class_var += 1  

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.class_var)
obj1.increment()
print(MyClass.class_var)
obj2.increment() 
print(MyClass.class_var)

# c. Static Methods
# Functions defined within a class but are not associated with any specific instance or the class itself.
class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
print(MathUtils.is_even(4))
print(MathUtils.is_prime(7))

# d. __init__ Method
# Special method in Python classes that is used to initialize the object's attributes when an instance of the class is created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)
print(person1.age) 

# e. __str __ Method
# special method in Python classes that is used to define the string representation of an object. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
person1 = Person("Alice", 25)
print(person1)
print(str(person1))

# f. __new__ Method
# The new method is a static method in Python classes that is called before the init method when creating a new instance of a class.
class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of Person")
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
person1 = Person("Alice", 25)
print(person1)

# 5. Methods with argument
# a. Pass object as an argument
class MyClass:
    def __init__(self, value):
        self.data = value

    def update(self, other):  
        self.data += other.data

obj1 = MyClass(10)
obj2 = MyClass(20)

obj1.update(obj2) 
print(obj1.data)

# b. Object as return type
class MyClass:
    def __init__(self, value):
        self.data = value

    def increment(self): 
        self.data += 1  
        return self

obj = MyClass(10)  
obj = obj.increment()
print(obj.data)

# c. Method overloading
class MyClass:
    def my_method(self, arg1, arg2=0):
        print(f"arg1: {arg1}, arg2: {arg2}")

obj = MyClass()
obj.my_method(10)  
obj.my_method(10, 20)
