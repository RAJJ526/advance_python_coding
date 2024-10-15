# from arrays import xnx,py



# print(py)


# import arrays  as r

# print(r.xnx)




# Python 3 code
# for i in range(5):
#     print(i)



# class Drive:
#     x="hello this is raj"
#     y="welcome to class method"
#     @classmethod
#     def func(cls):
#         print(cls.x, cls.y)
# obj=Drive()
# obj.func()

# class Delta:
#     v="the world is full of miseries"
#     def word(self):
#         print(self.v)
# r=Delta()
# r.word()

# class Perform:
#     c="the quieck jum over the lyz dog"
#     @classmethod
#     def func(cls):
#         print(cls.c)
# obj=Perform()
# obj.func()


# class Arraydddd:
#     v  =  'ooooooooooooooooooooooooooooo'
#     nup =  'gmkmgkfmgkfmgkfgmfkgmfkgmfkgm'

#     def y(self):
#         print(self.v,self.nup)

#     @classmethod
#     def dis(cls):
#         print(cls.v,cls.nup)

# Arraydddd().dis()
# a.dis()
# a.y()




# What is inheritance in Python?
# What is a base class and a derived class?
# How do you call the parent class’s method in a child class?
# What is method overriding?
# What is the super() function used for?
# Can you inherit multiple classes in Python?
# What is the difference between single inheritance and multiple inheritance? 
# How do you define an abstract class in Python?
# What is the __init__ method in inheritance?
# How do you prevent a class from being inherited?
# What is method resolution order (MRO)?
# Can you override methods in the parent class that are not implemented?
# How do you use the @staticmethod and @classmethod decorators in inheritance?
# class MathUtils:
#     @staticmethod
#     def add(x, y):
#         return x + y
# # Using the static method
# result = MathUtils.add(5, 3)
# print(result) 

# class MathUtils:
#     def add(x,y):
#         return x+y
# result=MathUtils.add(4,5)
# print(result)

# What happens if a child class does not call the parent class’s __init__ method?
# How do you access parent class attributes in a child class?

# Create a Base Class and a Derived Class:
# Define a base class Person with attributes name and age.
# Define a derived class Student that inherits from Person and adds an attribute student_id.
# class Person:
#     # def __init__(self,Student_id):
#     #     print(Student_id)
#     def display(self):
#         print("rajesh")
# class Student(Person):
#     def show(self):
#         pass
# obj=Student()
# obj.display()



# Create instances of both classes and print their attributes.0
# Method Overriding Example:

# Define a base class Shape with a method area that returns "Area method in Shape".

# class Shape:
#     def area(self):
#         return "Area method in Shape"
# obj=Shape()
# print(obj.area())

# Define a derived class Circle that overrides the area method to return the area of a circle (use a fixed radius for simplicity).

# # Create an instance of Circle and call the area method.
# import math
# # class Shape:
# #     def area(Self):
# #         raise SyntaxError("Subclass should be implemented this")
# class Circle():
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*(self.radius**2)
# my_circle=Circle(6)
# circle_area=my_circle.area()
# print(f'the area of my circle is', circle_area)

# # Using super() to Extend Functionality:

# # Define a base class Vehicle with an __init__ method that initializes make and model.
# class Vehicle:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#         print("let us define the make and model of vehicle")
#     def car(self):
#         return (f'{self.make} {self.model}')
# obj=Vehicle(make="Toyota" , model="beat")
# print(obj.car())

# # Define a derived class Car that extends Vehicle with an additional attribute number_of_doors.      
# # Base class
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
    
#     def __str__(self):
#         return f"{self.make} {self.model}"
# # Derived class
# class Car(Vehicle):
#     def __init__(self, make, model, number_of_doors):
#         super().__init__(make, model)  # Initialize base class attributes
#         self.number_of_doors = number_of_doors
#     def __str__(self):
#         # Override __str__ to include the number of doors
#         return f"{self.make} {self.model} with {self.number_of_doors} doors"
# # Example usage
# car = Car(make="Honda", model="Civic", number_of_doors=4)
# print(car)

# # Use the super() function in the Car class to call the Vehicle's __init__ method.
# class Vehicle:
#     def __init__(self,make, model):
#         self.make=make
#         self.model=model
# class Car(Vehicle):
#     def __str__(self,make,model):
#         super().__init__(make,model)
#     def __str__(self):
#         return f'{self.make}, {self.model}'
# obj=Car("Honda", "city")
# print(obj)
        

# # Create an instance of Car and print all its attributes.
# class Car():
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
# class Vehicle(Car):
#     def __str__(self,make,model):
#         super().__init__(make,model)
#     def __str__(self):
#         return f'{self.make}, {self.model}'
# obj=Vehicle("maruti", "swift")
# print(obj)









# Preventing Inheritance:

# Define a base class Immutable that has a method do_not_override.
# Prevent this class from being inherited by any other class.
# Try to create a derived class Attempted that inherits from Immutable and explain what happens.
# Multiple Inheritance Example:

# Define two base classes A and B, each with a method display.
# Define a derived class C that inherits from both A and B.
# Implement the display method in C to call both A's and B's display method

# class A:
#     def display(self):
#         print("kumar")
# class B:
#     def display(self,c,d):
#         print(c+d)      
# class C(A,B):
#     def display(self):
#         print("hwllo thghg ")
#         A.display(self)
#         B.display(self)
# obj=C()
# obj.display()


# # Create an instance of C and call its display method.
# # Abstract Base Classes (ABCs):

# # Define an abstract base class Animal with an abstract method make_sound.
# # Define two derived classes Dog and Cat that implement the make_sound method.
# # Base class
# class Animal:
#     def make_sound(self):
#         raise NotImplementedError("Subclasses should implement this method")
# class Dog(Animal):
#     def make_sound(self):
#         return "woof"
# class Cat(Animal):
#     def make_sound(self):
#         return "meow"
# def print_animal_sound(animal):
#     print(animal.make_sound())
# dog=Dog()
# cat=Cat()
# print_animal_sound(dog)
# print_animal_sound(cat)

# class Animal:
#     def make_sound(self):
#         raise NotImplementedError("Subclasses should implement this method")
# # Derived class Dog
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"
# # Derived class Cat
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
# # Example usage
# def print_animal_sound(animal):
#     print(animal.make_sound())

# # Create instances of Dog and Cat
# dog = Dog()
# cat = Cat()
# # Print the sounds
# print_animal_sound(dog)  # Output: Woof
# print_animal_sound(cat) 

# Create instances of Dog and Cat and call their make_sound methods.
# Using @classmethod and @staticmethod in Inheritance:

# Define a base class Book with a class method book_info and a static method is_book.
# Define a derived class EBook that inherits from Book.
# Override the book_info method in EBook to provide specific information for e-books.
# Call both book_info and is_book methods from instances of Book and EBook.
# Instance and Class Variables:

# Define a base class Counter with a class variable count and an instance variable value.

# Define a derived class AdvancedCounter that initializes value and increments the class variable count.

# Create instances of both classes and demonstrate how the class variable count changes.
# Constructor Chaining:

# Define a base class Base with a constructor that initializes a value.
# Define a derived class Derived that calls the Base constructor and adds additional initialization.
# Demonstrate how constructor chaining works by creating an instance of Derived.
# Using Inheritance to Extend Functionality:

# Define a base class Employee with methods for setting and getting employee details.


# Define a derived class Manager that adds additional functionality specific to managers (e.g., managing a team).
# Show how to use inheritance to extend the functionality of the base class.
# These questions cover a range of fundamental inheritance concepts and practical applications in Python programming.


# class Employee:
#     def __init__(self, name='', id_number='', position='', salary=0.0):
#         self._name = name
#         self._id_number = id_number
#         self._position = position
#         self._salary = salary

#     def set_name(self, name):
#         self._name = name

#     def get_name(self):
#         return self._name
    
#     def set_id_number(self, id_number):
#         self._id_number = id_number

#     def get_id_number(self):
#         return self._id_number

#     def set_position(self, position):
#         self._position = position

#     def get_position(self):
#         return self._position

#     def set_salary(self, salary):
#         self._salary = salary

#     def get_salary(self):
#         return self._salary

#     def __str__(self):
#         return (f'Employee(Name: {self._name}, ID: {self._id_number}, '
#                 f'Position: {self._position}, Salary: {self._salary})')

# # Create an instance of Employee
# emp = Employee(name='John Doe', id_number='12345', position='Software Engineer', salary=75000.0)

# # Get details
# print(emp.get_name())        # Output: John Doe
# print(emp.get_id_number())   # Output: 12345
# print(emp.get_position())    # Output: Software Engineer
# print(emp.get_salary())      # Output: 75000.0

# # Set new details
# emp.set_name('Jane Doe')
# emp.set_salary(80000.0)

# # Print updated details
# print(emp)  # Output: Employee(Name: Jane Doe, ID: 12345, Position: Software Engineer, Salary: 80000.0)



# # Define a derived class Manager that adds additional functionality specific to managers (e.g., managing a team).
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def __str__(self):
#         return f"Employee Name: {self.name}, ID: {self.id}"


# class Manager(Employee):
#     def __init__(self, name, id, team=None):
#         super().__init__(name, id)
#         self.team = team if team is not None else []

#     def add_team_member(self, employee):
#         if employee not in self.team:
#             self.team.append(employee)

#     def remove_team_member(self, employee):
#         if employee in self.team:
#             self.team.remove(employee)

#     def get_team(self):
#         return [str(member) for member in self.team]

#     def __str__(self):
#         team_info = ', '.join(self.get_team())
#         return f"Manager Name: {self.name}, ID: {self.id}, Team: [{team_info}]"

# # Example usage:
# emp1 = Employee("Alice", 101)
# emp2 = Employee("Bob", 102)

# mgr = Manager("Charlie", 201)
# mgr.add_team_member(emp1)
# mgr.add_team_member(emp2)

# print(mgr)
# mgr.remove_team_member(emp1)
# print(mgr)


# # Define a base class Counter with a class variable count and an instance variable value.
# class Counter:
#     # Class variable
#     count = 0
#     def __init__(self, value=0):
#         # Instance variable
#         self.value = value
#         # Increment the class variable count whenever a new instance is created
#         Counter.count += 1

#     def increment(self, amount=1):
#         """Increase the value of the counter by a specified amount."""
#         self.value += amount

#     def decrement(self, amount=1):
#         """Decrease the value of the counter by a specified amount."""
#         self.value -= amount

#     def get_value(self):
#         """Return the current value of the counter."""
#         return self.value

#     @classmethod
#     def get_count(cls):
#         """Return the current count of Counter instances."""
#         return cls.count
    
#     # Creating instances of Counter
# c1 = Counter()
# c2 = Counter(10)

# # Using instance methods
# c1.increment(5)
# c2.decrement(2)

# # Accessing instance variables
# print(c1.get_value())  # Output: 5
# print(c2.get_value())  # Output: 8

# # Accessing class variable through class method
# print(Counter.get_count())  # Output: 2













#parameterized constructor
# class A:
#     name2="Rajesh"
#     def __init__(self,age,name,address):
#         address="AMB"
#         print(age, name, address ,self.name2)
#     def show(self):
#         print(self.name2)
# obj=A(22,"Raj", None)
# obj.show()

#default constructor
# class A:
#     name="Suresh"
#     age=22
#     def __init__(self):
#         address="Jamshedpur"
#         print(self.name," ",address)
#     def Show(self):
#         print(self.age)
# obj=A()
# obj.Show()