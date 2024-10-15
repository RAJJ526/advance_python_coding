#make a class with the name of A inside A class solve the list sorting, make a B class inside B CLASS remove the duplicate element of list, make a C CLASS inside c class inherit A and B class with the help of C class use sort and remove list method.

#make a class with the name of A inside A class use instance and class variable and display the variable with the help of method

#make a class with the name of A inside the class make a function inside that funciton use args and kwargs variable


# class A:
#     def __init__(self):
#         print("road")

#     x=10
#     @classmethod
#     def func(cls):
#         print(cls.x)
    
#     @staticmethod
#     def delta(a,b):
#         print(a+b)

# obj=A()
# obj.func()
# obj.delta(4,5)


# class A:
#     def show(self,list):
#         x=sorted(list)
#         print(x)
# class B:
#     def display(self, list2):
#         for i in list2:
#             z=list2.count(i)
#             if z>1:
#                 list2.remove(i)
#         print(list2)
# class C(A,B):
#     pass
# list=[6,7,8,4,3,2,1]
# list2=[1,2,2,3,3,4,4,5,6,7,8,9]
# obj=C()
# obj.show(list)
# obj.display(list2)

# class A:
#     def __init__(self,list,kwargs):
#         self.list=list
#         self.kwargs=kwargs
#     def show(self,*args,**kwargs):
#         c=0
#         for i in args[0]:
#             c=c+i
#         print(c,kwargs['name'])
# list=[1,2,3,4]
# obj=A()
# obj.show(list,name='A')

# class A:
#     def show(self,**kwargs):
#         a=kwargs["Name"]
#         b=kwargs["age"]
#         print(a,b)
#     def kat(self,*args,**kwargs):
#         c=0
#         for i in args:
#             c=c+i
#         print(c,kwargs["Name"])
# list=[1,2,3,4]
# obj=A()
# obj.show(Name="RAJ", age=24)
# obj.kat(1,2,3,4,7,Name="sharma")

# class A:
#     x = 'kkkk'
#     @classmethod
#     def show(cls):
#         print(cls.x)
# obj=A()
# obj.show()

# class A:
#     def __init__(self, list):
#         self.list=list
#         print("sort the list")
#     def show(self):
#         z=sorted(self.list)
        
#         print(z,'-----------------------')
# class B:
#     def display(self,list2):
#         for i in list2:
#             z=list2.count(i)
#             if z>1:
#                 list2.remove(i)
#         print(list2)

# class C(A,B):
#     pass

        
# list=[1,2,5,6,7,4,3,2,9,4,3,2]
# list2=[1,2,2,3,3,4,4,5,6,7,8]
# obj=C(list)
# obj.display(list2)
# obj.show()
# obj=A(list)
# obj.show()
# xbj=B()
# xbj.display(list2)


#questions
# class A:
#     def show(self,l):
#         b=[]
#         for i in l:
#             if isinstance(i,list):
#                 b.extend(self.show(i))
#             else:
#                 b.append(i)
#         return b
# l=[1,2,3,4,[4,5,6,7,[5,6,7,8]]]
# obj=A()
# print(obj.show(l))
    

#remove unnencessary elements
# class A:
#     def show(self,li):
#         a=0
#         while True:
#             x=True
#             for i in li:
#                 if isinstance(i,list):
#                     x=False
#                 elif isinstance(i,tuple):
#                     x=False
#             if x:
#                 break
#             if isinstance(li[a],list):
#                 li.remove(li[a])
#                 continue
#             elif isinstance(li[a],tuple):
#                 li.remove(li[a])
#                 continue
#             a=a+1
#         print(li)
# li=[1,2,3,[3,4,5],5,6,7,33,44,(4,5,6)]
# obj=A()
# obj.show(li)
        

#print duplicate elements and how many times it come
# class Duplicate:
#     def display(self,list):
#         d={}
#         for i in list:
#             if i in d:
#                 d[i]=d[i]+1
#             else:
#                 d[i]=1
#         print(d)
# class Copy(Duplicate):
#     pass
# list=[1,2,2,3,3,4,4,5,6,7,7,8,9,66,77,88,88]
# lkg=Copy()
# lkg.display(list)

#local global variables
# class A:
#     a=20
#     @classmethod
#     def show(cls):
#         global a
#         print(cls.a)
# obj=A()
# obj.show()

#recursion
# class B:
#     a=0
#     def recur(self):
#         global a
#         self.a=self.a+1
#         print(self.a)
#         self.recur()
# obj=B()
# obj.recur()

#sum of list in  a list
# class Delta:
#     def display(self,l):
#         b=0
#         for i in l:
#             if isinstance(i,list):
#                 b=b+self.display(i)
#             else:
#                 b=b+i
#         return b
# l=[1,2,3,4,[5,6,7,8,[4,5,6,7]]]
# obj=Delta()
# print(obj.display(l))

#handle mulitple inheritance in python
# class A:
#     def display(self):
#         print("class is missed")
# class B:
#     def display(self):
#         print("class is ready")
# class C(A,B):
#     def display(self):
#         print("lets go")
#         A.display(self)
#         B.display(self)
# obj=C()
# obj.display()

#create an instance of a circle with area method
#or find the area of circle
# class Circle:
#     def __init__(self, radius):
#         self.radius=radius
#         print("let us find the area of circle")
#     def area(self):
#         return 3.14*(self.radius**2)
# obj=Circle(2)
# print(obj.area())

# Define a base class Vehicle with an __init__ method that initializes make and model.
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def car(self):
        return f"{self.make} and {self.model}"
obj=Vehicle(model="Swift", make="Maruti")
print(obj.car())

# Define a derived class Car that extends Vehicle with an additional attribute number_of_doors.
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
class Car(Vehicle):
    def __init__(self,make,model,number_of_doors):
        super().__init__(make,model)
        # self.make=make
        # self.model=model
        self.number_of_doors=number_of_doors
    def __str__(self):
        return f'{self.make} {self.model} {self.number_of_doors}'
car=Car("toyota","beat", 4)
print(car)


# Use the super() function in the Car class to call the Vehicle's __init__ method.
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        print('----')
class Car(Vehicle):
    def __init__(self,make,model,number_of_doors):
        super().__init__(make,model)
        self.number_of_doors=number_of_doors
        print('==============')  
car=Car("maruti", "ciaz", 55)
print(car,'----------------------------------------------------------------------------')


# # Define two derived classes Dog and Cat that implement the make_sound method.
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method")
# Derived class Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof"
# Derived class Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow"
# Example usage
def dash(animal):
    print(animal.make_sound())
# Create instances of Dog and Cat
dog = Dog()
cat = Cat()
# Print the sounds
dash(dog)  # Output: Woof
dash(cat) 


# class Animal:
#     pass
class Dog():
    def make_sound(self):
        return "bow bow"
class Cat():
    def make_sound(self):
        return "Meoooowww"
def kat(shelu):
    print(shelu.make_sound())
dog=Dog()
cat=Cat()
kat(dog)
kat(dog)


#get employees details using inheritance
class Employee:
    def __init__(self, name='', id_number='', position='', salary=0.0):
        self._name = name
        self._id_number = id_number
        self._position = position
        self._salary = salary
        
    # def set_name(self, name):
    #     self._name = name

    def get_name(self):
        return self._name

    # def set_id_number(self, id_number):
    #     self._id_number = id_number

    def get_id_number(self):
        return self._id_number

    # def set_position(self, position):
    #     self._position = position

    def get_position(self):
        return self._position

    # def set_salary(self, salary):
    #     self._salary = salary

    def get_salary(self):
        return self._salary

    def __str__(self):
        return (f'Employee(Name: {self._name}, ID: {self._id_number}, '
                f'Position: {self._position}, Salary: {self._salary})')

# Create an instance of Employee
emp = Employee(name='John Doe', id_number='12345', position='Software Engineer', salary=75000.0)

# Get details
print(emp.get_name())        # Output: John Doe
print(emp.get_id_number())   # Output: 12345
print(emp.get_position())    # Output: Software Engineer
print(emp.get_salary())      # Output: 75000.0
print(emp)
# Set new details
# emp.set_name('Jane Doe')
# emp.set_salary(80000.0)
# Print updated details
# print(emp)  # Output: Employee(Name: Jane Doe, ID: 12345, Position: Software Engineer, Salary: 80000.0)




class Employee:
    def __init__(self,name,id, position, salary):
        self.name=name
        self.id=id
        self.position=position
        self.salary=salary
        print("let us gather employee data")
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_salary(self):
        return self.salary
    def __str__(self):
        return f'(Name: {self.name}, position: {self.position}, Salary: {self.salary})'

emp=Employee(name="Raj Kumar", position="Software Engineer", salary=100000,id=45)
print(emp.get_name())
print(emp.get_id())
print(emp)

    






    

    
    

            



        
