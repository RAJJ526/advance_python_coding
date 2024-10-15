# class A:
#     def show(self,name,age,gender):
#         if name is  None and age is None:
#             return (name,age)
#         elif name is not None and age is None:
#             return (name)
#         elif gender is not None:
#             return age
# obj=A()
# print(obj.show(name="Raj", age=24, gender="male"))
# print(obj.show(name="Rajesh",age=None, gender="male"))


# class B:
#     def display(self, gender="",age=""):
#         print("welcome",gender,age)
# obj=B()
# obj.display("male")
# obj.display("male", 24)



























# #example 2
# # First product method.
# # Takes two argument and print their
# # product
# def product(a, b):
#     p = a * b
#     print(p)
# # Second product method
# # Takes three argument and print their
# # product
# def product(a, b, c):
#     p = a*b*c
#     print(p)
# # Uncommenting the below line shows an error
# # product(4, 5)
# # This line will call the second product method
# product(4, 5, 5)


# #example 3
# # Function to take multiple arguments
# def add(datatype, *args):
#     # if datatype is int
#     # initialize answer as 0
#     if datatype == 'int':
#         answer = 9
#     # if datatype is str
#     # initialize answer as ''
#     if datatype == 'str':
#         answer = ""
#     # Traverse through the arguments
#     for x in args:
#         # This will do addition if the
#         # arguments are int. Or concatenation
#         # if the arguments are str
#         answer = answer + x
#     print(answer)
# # Integer
# add('int', 5, 6)

# # String
# # add('str', 'Hi ', 'Geeks')

# #example 4
# class Solution:
#     def display(self,dex,*args):
#         if dex=="int":
#             answer =5
#         elif dex=="str":
#           answer="raju"
#         else:
#             answer=0
#         for i in args:
#             answer=answer+i
#         print(answer)
# xyz=Solution()
# xyz.display("int", 5,6,7,8)





 

