# class Animal:
#     def speak(self):
#         return "Some generic animal sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# # Create instances of Animal, Dog, and Cat
# generic_animal = Animal()
# dog = Dog()
# cat = Cat()
# # Call the speak method on each instance
# print("Animal says:", generic_animal.speak())  # Output: Some generic animal sound
# print("Dog says:", dog.speak())                # Output: Woof!
# print("Cat says:", cat.speak())                # Output: Meow!



#example 2
# class Shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y
# class Area(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def area(self):
#         return 3.14* super().area()
# obj=Area(5)
# print(obj.area())



# class Shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y
# class Point(Shape):
#     def __init__(self,radius):
        
#         super().__init__(radius,radius)

#     def area(self):
#         return 3.14* super().area()
# obj=Point(5)
# print(obj.area())


# class Shape:
#     def area(self,x,y):
#         return x*y
# class Area(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().area(self.radius,self.radius)
#     def area(self):
#         return 3.14* super().area()
# obj=Area(5)
# print(obj.area())


#method overriding example
# class A:
#     def show(self,a,b):
#         return a+b

# class B(A):
#     def show(self,a,b):
#         return a-b

# obj1=A()
# obj2=B()
# print(obj1.show(3,4))
# print(obj2.show(5,6))


# class A:
#     def show(self,a,b):
#         return a+b
# class B(A):
#     def show(self,a,b):
#         return a-b
# obj1=A()
# obj2=B()
# print(obj2.show(3,4))














    




