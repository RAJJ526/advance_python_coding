# #example1
class A:
    def add(self):
        print("hello world")
class B(A):
    def show(self):
        super().add()
x=B()
x.show()

# #example2
# class A:
  
#   def __init__(self,a,b):
#       self.a=a
#       self.b=b
# class B():
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c=c
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c}'
# x=B(4,5,6)
# print(x)

#example3
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def show(self, fname, lname):
#     super().__init__(fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()



