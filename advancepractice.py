
# a="fjgkgigofMDLFLFFkfkfllglgl"
# print(a.replace("F","f"))

# # Define two derived classes Dog and Cat that implement the make_sound method.
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
# def dash(animal):
#     print(animal.make_sound())
# # Create instances of Dog and Cat
# dog = Dog()
# cat = Cat()
# # Print the sounds
# dash(dog)  # Output: Woof
# dash(cat) 


# class Animal:
#     pass
# class Dog():
#     def make_sound(self):
#         return "bow bow"
# class Cat():
#     def make_sound(self):
#         return "Meoooowww"
# def kat(shelu):
#     print(shelu.make_sound())
# dog=Dog()
# cat=Cat()
# kat(dog())
# kat(dog())

# class Goat:
#     def show(self):
#         return "hello from goat"
# class Fox:
#     def show(self):
#         return "hello fox is here"
# def test(delta):
#     print(delta.show())

# x=Goat()
# y=Fox()
# test(x)
# test(y)


# Define two derived classes Dog and Cat that implement the make_sound method.
# class Dog:
#     def show(self):
#         return "bark"
# class Cat:
#     def show(self):
#         return "meow"
# def display(animal):
#     print(animal.show())
# A=Dog()
# B=Cat()
# display(A)
# display(B)

#duck duck typing
# class Dog:
#     def show(self):
#         print("hello world")
# class Cat:
#     def show(Self):
#         print("deport")
# def run(*args):
#         for i in args:
#             i.show()
# A=Dog()
# B=Cat()
# run(A,B)

#duck duck typing
# class Dog:
#     def show(Self):
#         print("has attribute")
# class Bod:
#     def display(self):
#         print("let it be")

# if hasattr(Bod,"display"):
#     Bod().display()
# else:
#     Dog().show()

#create an instance of a car and print all its attributes
# class Car:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#         print("let us define the make and model of a car")
# class Vehicle(Car):
#     def show(self,make,model):
#        super().__init__(make,model)
#     def __str__(self):
#        return f'{self.make}, {self.model}'
# A=Vehicle(make="toyota", model="beat")
# print(A)

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
        
# Create an instance of Circle and call the area method.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#         print("let us calculate the radius of a circle")
#     def area(self):
#         return math.pi*(self.radius**2)
# A=Circle(5)
# print(A.area())
        
# Create an instance of Rectangle and call the area method.
# class Rectangle:
#         def __init__(self,length,breadth):
#             self.length=length
#             self.breadth=breadth
#             print("let us calculate area of rectangle")
#         def area(self):
#               return self.length*self.breadth
# obj=Rectangle(4,2)
# print(obj.area())
              


# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*(self.radius**2)
#     def perimeter(self):
#         return 2*math.pi* self.radius

# radius=float(input("enter the radius of circle"))    
# obj=Circle(radius)
# Area=obj.area()
# Permeter=obj.perimeter()
# print("Area of Circle is", Area)
# print("Perimeter of Circle is", Permeter)


#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# Define a class called Calculator to perform basic arithmetic operations
# class Calculator:
#     # Define a method for addition that takes two arguments and returns their sum
#     def add(self, x, y):
#         return x + y

#     # Define a method for subtraction that takes two arguments and returns their difference
#     def subtract(self, x, y):
#         return x - y

#     # Define a method for multiplication that takes two arguments and returns their product
#     def multiply(self, x, y):
#         return x * y

#     # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
#     # or an error message if the denominator is zero
#     def divide(self, x, y):
#         if y != 0:
#             return x / y
#         else:
#             return ("Cannot divide by zero.")

# # Example usage
# # Create an instance of the Calculator class
# calculator = Calculator()

# # Perform addition and print the result
# result = calculator.add(7, 5)
# print("7 + 5 =", result)

# # Perform subtraction and print the result
# result = calculator.subtract(34, 21)
# print("34 - 21 =", result)

# # Perform multiplication and print the result
# result = calculator.multiply(54, 2)
# print("54 * 2 =", result)

# # Perform division and print the result
# result = calculator.divide(144, 2)
# print("144 / 2 =", result)

# # Attempt to perform division by zero, which raises an error, and print the error message
# result = calculator.divide(45, 0)
# print("45 / 0 =", result)


#example
# class Calculator:
#     def add(self,x,y):
#         return x+y
#     def subtract(self,x,y):
#         return x-y
#     def multiply(self,x,y):
#         return x*y
#     def divide(Self,x,y):
#        if y!=0:
#            return x/y
#        else:
#            return ("cannot divide by zero")
# obj=Calculator()
# a=obj.add(4,5)
# print("4+5 =",a)
# b=obj.subtract(6,4)
# print("6-4=",b)
# c=obj.multiply(3,3)
# print("3*3=",c)
# d=obj.divide(4,2)
# print("4/2=", d)


#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# class Calculator:
#     def add(self,x,y):
#         return x+y
    
#     def subtract(self,x,y):
#         return x-y
    
#     def multiply(self,x,y):
#         return x*y
    
#     def divide(self,x,y):
#         if y!=0:
#             return x/y
#         else:
#             return ("cannot divide by zero")

# calculate=Calculator()
# print("7+5=", calculate.add(7,5))
# print("7-5=", calculate.subtract(7,5))
# print("7*5=", calculate.multiply(7,5))
# print("10/0=", calculate.divide(10,0))



# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

# #Import the math module to access mathematical functions like pi
# import math

# # Define a base class called Shape to represent a generic shape with methods for calculating area and perimeter
# class Shape:
#     # Placeholder method for calculating area (to be implemented in derived classes)
#     def calculate_area(self):
#         pass

#     # Placeholder method for calculating perimeter (to be implemented in derived classes)
#     def calculate_perimeter(self):
#         pass

# # Define a derived class called Circle, which inherits from the Shape class
# class Circle():
#     # Initialize the Circle object with a given radius
#     def __init__(self, radius):
#         self.radius = radius

#     # Calculate and return the area of the circle using the formula: π * r^2
#     def calculate_area(self):
#         return math.pi * self.radius**2

#     # Calculate and return the perimeter of the circle using the formula: 2π * r
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius

# # Define a derived class called Rectangle, which inherits from the Shape class
# class Rectangle(Shape):
#     # Initialize the Rectangle object with given length and width
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     # Calculate and return the area of the rectangle using the formula: length * width
#     def calculate_area(self):
#         return self.length * self.width

#     # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)

# # Define a derived class called Triangle, which inherits from the Shape class
# class Triangle(Shape):
#     # Initialize the Triangle object with a base, height, and three side lengths
#     def __init__(self, base, height, side1, side2, side3):
#         self.base = base
#         self.height = height
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3

#     # Calculate and return the area of the triangle using the formula: 0.5 * base * height
#     def calculate_area(self):
#         return 0.5 * self.base * self.height

#     # Calculate and return the perimeter of the triangle by adding the lengths of its three sides
#     def calculate_perimeter(self):
#         return self.side1 + self.side2 + self.side3

# # Example usage
# # Create a Circle object with a given radius and calculate its area and perimeter
# r = 7
# circle = Circle(r)
# circle_area = circle.calculate_area()
# circle_perimeter = circle.calculate_perimeter()

# # Print the results for the Circle
# print("Radius of the circle:", r)
# print("Circle Area:", circle_area)
# print("Circle Perimeter:", circle_perimeter)

# # Create a Rectangle object with given length and width and calculate its area and perimeter
# l = 5
# w = 7
# rectangle = Rectangle(l, w)
# rectangle_area = rectangle.calculate_area()
# rectangle_perimeter = rectangle.calculate_perimeter()

# # Print the results for the Rectangle
# print("\nRectangle: Length =", l, " Width =", w)
# print("Rectangle Area:", rectangle_area)
# print("Rectangle Perimeter:", rectangle_perimeter)

# # Create a Triangle object with a base, height, and three side lengths, and calculate its area and perimeter
# base = 5
# height = 4
# s1 = 4
# s2 = 3
# s3 = 5

# # Print the results for the Triangle
# print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
# triangle = Triangle(base, height, s1, s2, s3)
# triangle_area = triangle.calculate_area()
# triangle_perimeter = triangle.calculate_perimeter()
# print("Triangle Area:", triangle_area)
# print("Triangle Perimeter:", triangle_perimeter)



# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

# import math
# class Shape:
#     def calculate_area(Self):
#         pass
#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def calculate_area(self):
#         return math.pi*(self.radius**2)
#     def calculate_perimeter(self):
#         return 2* math.pi*(self.radius)
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def calculate_area(self):
#         return self.l*self.b
#     def calculate_perimeter(self):
#         return 2* (self.l+self.b)
# class Triangle(Shape):
#     def __init__(self,base,height,side1,side2,side3):
#         self.base=base
#         self.height=height
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3
#     def calculate_area(self):
#         return 0.5*self.base*self.height
#     def calculate_perimeter(self):
#         return self.side1+self.side2+self.side3
    
# obj=Circle(5)
# x=obj.calculate_area()
# y=obj.calculate_perimeter()
# print("area of circle is ", x)
# print("perimeter of circle is ", y)

# job=Rectangle(5,6)
# a=job.calculate_area()
# b=job.calculate_perimeter()
# print("area of rectangle is ", a)
# print("perimter of rectangle is ", b)

# dob=Triangle(3,4,6,6,6)
# m=dob.calculate_area()
# n=dob.calculate_perimeter()
# print("area of triangle is ", m)
# print("perimeter of triangle is ", n)


# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

# import math
# class Shape:
#     def calculate_area(self):
#         pass

#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
    
#     def calculate_area(self):
#         return math.pi*(self.radius**2)
    
#     def calculate_perimeter(self):
#         return 2*math.pi*self.radius

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def calculate_area(self):
#         return self.l*self.b
    
#     def calculate_perimeter(self):
#         return 2*(self.l+self.b)
    
# class Triangle(Shape):
#     def __init__(self,base, height, side1, side2, side3):
#         self.base=base
#         self.height=height
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3

#     def calculate_area(self):
#         return 0.5*self.base*self.height
    
#     def calculate_perimeter(self):
#         return self.side1*self.side2*self.side3
    

# obj1=Circle(5)
# obj2=Rectangle(4,5)
# obj3=Triangle(3,4,5,6,7)

# print("Area of Circle is", obj1.calculate_area())
# print("Perimeter of Circle is", obj1.calculate_perimeter())

# print("\r")

# print("Area of Rectangle is", obj2.calculate_area())
# print("Perimeter of Rectangle is", obj2.calculate_perimeter())

# print("\r")


# print("Area of Triangle is", obj3.calculate_area())
# print("Perimeter of Triangle is", obj3.calculate_perimeter())



# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
# Define a class called Bank to implement a simple banking system
# class Bank:
#     # Initialize the bank with an empty dictionary to store customer accounts and balances
#     def __init__(self):
#         self.customers = {}

#     # Create a new account with a given account number and an optional initial balance (default to 0)
#     def create_account(self, account_number, initial_balance=0):
#         if account_number in self.customers:
#             print("Account number already exists.")
#         else:
#             self.customers[account_number] = initial_balance
#             print("Account created successfully.")

#     # Make a deposit to the account with the given account number
#     def make_deposit(self, account_number, amount):
#         if account_number in self.customers:
#             self.customers[account_number] = self.customers[account_number] + amount
#             print("Deposit successful.")
#         else:
#             print("Account number does not exist.")
       

#     # Make a withdrawal from the account with the given account number
#     def make_withdrawal(self, account_number, amount):
#         if account_number in self.customers:
#             if self.customers[account_number] >= amount:
#                 self.customers[account_number] -= amount
#                 print("Withdrawal successful.")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Account number does not exist.")

#     # Check and print the balance of the account with the given account number
#     def check_balance(self, account_number):
#         if account_number in self.customers:
#             balance = self.customers[account_number]
#             print(f"Account balance: {balance}")
#         else:
#             print("Account number does not exist.")

# # Example usage
# # Create an instance of the Bank class
# bank = Bank()

# # Create customer accounts and perform account operations
# acno1= "SB-123"
# damt1 = 1000
# print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
# bank.create_account(acno1, damt1)

# acno2= "SB-124"
# damt2 = 1500
# print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
# bank.create_account(acno2, damt2)

# wamt1 = 600
# print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
# bank.make_deposit(acno1, wamt1)

# wamt2 = 350
# print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
# bank.make_withdrawal(acno2, wamt2)

# print("A/c. No.",acno1)
# bank.check_balance(acno1)

# print("A/c. No.",acno2)
# bank.check_balance(acno2)

# wamt3 = 1200
# print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
# bank.make_withdrawal(acno2, wamt3)

# acno3 = "SB-134"
# print("A/c. No.",acno3)
# bank.check_balance(acno3)  # Non-existent account number 




# Define a class called Bank to implement a simple banking system

# class Bank:
#     def __init__(self):
#         self.customers={}

#     def create_account(self, account_number,initial_balance):
#         if account_number in self.customers:
#             print("account number already exists")
#         else:
#             self.customers[account_number]=initial_balance
#             print("account created successfully", "Account_number-", account_number, "deposit amount-", initial_balance)

#     def make_deposit(self,account_number,amount):
#         if account_number in self.customers:
#             self.customers[account_number]=self.customers[account_number]+amount
#             print("amount deposit successful")
#         else:
#             print("account number does not exist")

#     def with_drawl(self,account_number,amount):
#         if account_number in self.customers:
#             if self.customers[account_number]>=amount:
#                 self.customers[account_number]=self.customers[account_number]-amount
#                 print("account withdrawl succesfull of Rs. ", amount)
#             else:
#                 print("insufficient balance")
#         else:
#             print("account number does not exist")
        

#     def check_balance(self,account_number):
#         if account_number in self.customers:
#             balance=self.customers[account_number]
#             print("current balance is ", balance)
#         else:
#             print("account number does not exist")

# bank = Bank()
# bank.create_account("PBI-1", 1000)
# bank.make_deposit("PBI-1", 500)
# bank.with_drawl("PBI-1", 200)
# bank.check_balance("PBI-1")
# bank.with_drawl("PBI-1",400)
# bank.check_balance("PBI-1")
# bank.create_account("PBI-2", 700)


# class Bank:
#     def __init__(self):
#         self.customers={}

#     def create_account(self,account_number,initial_balance=0):
#         if account_number in self.customers:
#             print("account number already exists")
#         else:
#             self.customers[account_number]=initial_balance
#             print("your account successfully created")
            
#     def money_deposit(self,account_number, amount):
#         if account_number in self.customers:
#             self.customers[account_number]=self.customers[account_number]+amount
#             print("money deposit successfully of amount", amount)
    
#     def money_withdrawl(self,account_number,amount):
#         if account_number in self.customers:
#             if self.customers[account_number]>=amount:
#                 self.customers[account_number]=self.customers[account_number]-amount
#                 print("money withdrawl of amount", amount)
#             else:
#                 print("insufficient fund")
#         else:
#             print("account number not exist")

#     def check_balance(self,account_number):
#         if account_number in self.customers:
#             balance=self.customers[account_number]
#             print("your current balance is ", balance)
#         else:
#             print("account number not exist")

# obj=Bank()
# obj.create_account("SBI-1", 1000)
# obj.money_deposit("SBI-1", 500 )
# obj.money_withdrawl("SBI-89", 300)
# obj.check_balance("SBI-1")



# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
# class Bank:
#     def __init__(self):
#         self.customers={}

#     def create_account(self,account_number,initial_balance):
#         if account_number in self.customers:
#             print("account already exists")
#         else:
#             self.customers[account_number]=initial_balance
#             print("account created successfully")

#     def add_amount(self,account_number,amount):
#         if account_number in self.customers:
#             self.customers[account_number]=self.customers[account_number]+amount
#             print("Amount deposited successfully")
#         else:
#             print("account number does not exist")

#     def withdrawl_amount(self,account_number,amount):
#         if account_number in self.customers:
#             if self.customers[account_number]>=amount:
#                 self.customers[account_number]-=amount
#                 print("Amount deducted successfully")
#             else:
#                 print("insufficient funds")
#         else:
#             print("account number does not exist")

#     def check_balance(self,account_number):
#         if account_number in self.customers:
#             print("your account balance is ", self.customers[account_number])
#         else:
#             print("account number does not exist")

# obj=Bank()
# obj.create_account("Raj", 1000)
# obj.create_account("Rajesh", 2000)
# obj.create_account("Arun", 3000)
# obj.create_account("Sameer", 1000)
# print(obj.customers)

# obj.add_amount("Raj", 300)
# print(obj.customers)

# obj.withdrawl_amount("Rajesh", 200)
# print(obj.customers)

# x=obj.check_balance("Sameer")





# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
# Define a class called Stack to implement a stack data structure
# class Stack:
    # Initialize the stack with an empty list to store items
#     def __init__(self):
#         self.items = []

#     # Push an item onto the stack
#     def push(self, item):
#         self.items.append(item)

#     # Pop (remove and return) an item from the stack if the stack is not empty
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Cannot pop from an empty stack.")

#     # Check if the stack is empty
#     def is_empty(self):
#         return len(self.items) == 0

#     # Display the items in the stack
#     def display(self):
#         print("Stack items:", self.items)

# # Example usage
# # Create an instance of the Stack class
# stack = Stack()

# # Push items onto the stack
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)

# # Display the items in the stack
# stack.display()

# # Pop items from the stack and print the popped items
# popped_item = stack.pop()
# print("Popped item:", popped_item)
# popped_item = stack.pop()
# print("Popped item:", popped_item)

# #check the length of the stack if stack is empty it returns true otherwise returns false
# x=stack.is_empty()
# print("the length of stack is", x)

# # Display the updated items in the stack
# stack.display()


# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
# class Stack:
#     def __init__(self):
#         self.items=[]

#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Cannot pop from empty list")
        
#     def is_empty(self):
#         return len(self.items)==0
    
#     def display(self):
#         print("stack items", self.items)

# stack=Stack()
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)
# stack.push(60)
# stack.display()
# print("popped item: ", stack.pop())
# print("popped item: ", stack.pop())
# print("check stack: " , stack.is_empty())
# stack.display()
# print(stack.items)
     
    
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
# class Stack:
#     def __init__(self):
#         self.items=[]

#     def add(self,element):
#         self.items.append(element)
    
#     def remove(self):
#         if not self.is_empty():
#            return self.items.pop()
        
#     def is_empty(self):
#         return len(self.items)==0
    
#     def display(self):
#         return self.items
    
# obj=Stack()
# obj.add(30)
# obj.add(40)
# obj.add(50)
# obj.add(60)
# obj.add(70)
# obj.add(80)
# print(obj.display())
# print(obj.remove())
# print(obj.items)
# print(obj.is_empty())
    

# Define a class called Queue to implement a queue data structure
# class Queue:
#     # Initialize the queue with an empty list to store items
#     def __init__(self):
#         self.items = []

#     # Add (enqueue) an item to the end of the queue
#     def enqueue(self, item):
#         self.items.append(item)

#     # Remove and return (dequeue) an item from the front of the queue if the queue is not empty
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             raise IndexError("Cannot dequeue from an empty queue.")

#     # Check if the queue is empty
#     def is_empty(self):
#         return len(self.items) == 0

# # Example usage
# # Create an instance of the Queue class
# queue = Queue()

# # Enqueue (add) items to the queue
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)

# # Print the current items in the queue
# print("Current Queue:", queue.items)

# # Dequeue (remove) items from the front of the queue and print the dequeued items
# dequeued_item = queue.dequeue()
# print("Dequeued item:", dequeued_item)
# dequeued_item = queue.dequeue()
# print("Dequeued item:", dequeued_item)

# # Print the updated items in the queue
# print("Updated Queue:", queue.items) 



# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
# class Queue:
#     def __init__(self):
#         self.queue=[]

#     def enqueue(self,element):
#         self.queue.append(element)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         else:
#             raise IndexError("cannot pop from empty queue")
        
#     def is_empty(self):
#         return len(self.queue)==0
    
#     def display(self):
#         return self.queue
    
# obj=Queue()
# obj.enqueue(50)
# obj.enqueue(60)
# obj.enqueue(70)
# obj.enqueue(80)
# obj.enqueue(90)
# obj.display()

# print(obj.dequeue())
# print(obj.dequeue())
# print(obj.dequeue())

# print(obj.is_empty())
# print("remaininign elements", obj.queue)


# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
# class Queue:
#     def __init__(self):
#         self.queue=[]

#     def add(self,element):
#         self.queue.append(element)

#     def remove(self,element):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         else:
#             raise IndexError("Cannot remove from empty queue.")
        
        
#     def is_empty(self):
#         return len(self.queue)==0
    
#     def display(self):
#         return self.queue
    
# obj=Queue()
# obj.add("food")
# obj.add("grapes")
# obj.add("banana")
# obj.add("pomegrate")
# print(obj.queue)

# obj.remove("food")
# print(obj.queue)

# x=obj.is_empty()
# print(x)

# print(obj.display())


# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# Define a class called ShoppingCart to represent a shopping cart
# class ShoppingCart:
#     # Initialize the shopping cart with an empty list of items
#     def __init__(self):
#         self.items = []

#     # Add an item with a name and quantity to the shopping cart
#     def add_item(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)

#     # Remove an item with a specific name from the shopping cart
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break

#     # Calculate and return the total quantity of items in the shopping cart
#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         return total

# # Example usage
# # Create an instance of the ShoppingCart class
# cart = ShoppingCart()

# # Add items to the shopping cart
# cart.add_item("Papaya", 100)
# cart.add_item("Guava", 200)
# cart.add_item("Orange", 150)


# # Display the current items in the cart and calculate the total quantity
# print("Current Items in Cart:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

# # Remove an item from the cart, display the updated items, and recalculate the total quantity
# cart.remove_item("Orange")
# print("\nUpdated Items in Cart after removing Orange:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty) 


# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# class Product:
#     def __init__(self):
#         self.items=[]

#     def add(self,item_name, quantity):
#         item=(item_name,quantity)
#         self.items.append(item)

#     def remove(self,item_name):
#         for item in self.items:
#             if item[0]==item_name:
#                 self.items.remove(item)
#                 break

#     def calculate(self):
#         total=0
#         for item in self.items:
#             total=total+item[1]
#         return total
    
# obj=Product()
# obj.add("Bread", 100)
# obj.add("Butter", 250)
# obj.add("Jam", 300)
# obj.add("Sugar", 150)
# obj.add("Chocolate", 600)

# print("cart items")

# for i in obj.items:
#     print(i[0], "-" , i[1])

# print("\r")
# print("cart items after remove  item bread")
# obj.remove("Bread")
# for i in obj.items:
#     print(i[0], "-" , i[1])

# print("\r")
# print("total price")
# x=obj.calculate()
# print(x)


# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# class Product:
#     def __init__(self):
#         self.items=[]

#     def add_item(self,item_name,quantity):
#         item=(item_name,quantity)
#         self.items.append(item)
    
#     def remove_item(self,item_name):
#         for item in self.items:
#             if item[0]==item_name:
#                 self.items.remove(item)
#                 break
    
#     def calculate_total_price(self):
#         total=0
#         for item in self.items:
#             total = total+item[1]
#             return total
        
# obj=Product()
# x=obj.add_item("Bread", 100)
# y=obj.add_item("choclate", 300)
# z=obj.add_item("biscuit", 150)
# a=obj.add_item("cake", 180)
# b=obj.add_item("cherry", 200)

# print(obj.items)
# print("cart items")
# for i in obj.items:
#     print(i[0], "-", i[1])
# obj.remove_item("cake")
# print(obj.items)
# k=obj.calculate_total_price()
# print("total price")
# print(k)


# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
# Import the date class from the datetime module to work with dates
# from datetime import date

# # # # Define a class called Person to represent a person with a name, country, and date of birth
# class Person:
#     # Initialize the Person object with a name, country, and date of birth
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
    
#     # Calculate the age of the person based on their date of birth
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# # Example usage
# # Create three Person objects with different attributes
# person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
# person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
# person3 = Person("Elizaveta Tilman", "USA", date(2026, 1, 1))

# # Access and print the attributes and calculated age for each person
# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of_birth)
# print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of_birth)
# print("Age:", person2.calculate_age())

# print("\nPerson 3:")
# print("Name:", person3.name)
# print("Country:", person3.country)
# print("Date of Birth:", person3.date_of_birth)
# print("Age:", person3.calculate_age())


# from datetime import date
# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth
    
#     def calculate_age(self):
#         today=date.today()
#         age=today.year-self.date_of_birth.year
#         return age
    
# obj1=Person("Raj Kumar", "India", date(2000,3,18))
# obj2=Person("Kartik", "Verma", date(1983,12,13))
# obj3=Person("Mahesh", "USA", date(1995,6,23))

# print("the person1 age is",obj1.calculate_age())
# print("the person 1 name is", obj1.name)
# print("his date of birth is ", obj1.date_of_birth)
# print("\r")
# print("the person2 age is ", obj2.calculate_age())
# print("the person 1 name is", obj2.name)
# print("his date of birth is ", obj2.date_of_birth)
# print("\r")
# print("the person3 age is ", obj3.calculate_age())
# print("the person 1 name is", obj3.name)
# print("his date of birth is ", obj3.date_of_birth)
# print("\r")

        
# from datetime import date
# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth

#     def calculate(self):
#         today=date.today()
#         age=today.year-self.date_of_birth.year
#         return age
    

# person1=Person("Raj Kumar", "India", date(2000,3,18))
# x=person1.calculate()
# print("The person 1 name is ", person1.name, "and the age is " , x )
# person2=Person("Aryan", "India", date(1994,6,12))
# y=person2.calculate()
# print("The person 2 name is ", person2.name, "and the age is " , y )






# class Calculator:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     def calculator(self):
#         if self.z=='+':
#             print(self.x+self.y)
#         elif self.z=="-":
#             print(self.x-self.y)
#         elif self.z=="*":
#             print(self.x*self.y)
#         elif self.z=="/":
#             print(self.x/self.y)

# x=float(input("enter first number"))
# y=float(input("enter second number"))
# z=input("enter the operation you want to perform")
# obj=Calculator(x,y,'+')
# obj.calculator()


    
       


        

























