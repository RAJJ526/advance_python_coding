#simple inheritance
# class Parent:
#     def property(self):
#         print("1 cr")
# class Child(Parent):
#     def dis(self):
#         print("my name is Raj")
# B=Child()
# B.property()

#multilevel inheritance
# class GParent():
#     def property(self):
#         print("1 cr")
# class Parent(GParent):
#     def name(self):
#         print("Raj")
# class Child(Parent):
#     def indo(self):
#         print("name is xyz")
# A=Child()
# A.name()
# A.property()

#hybrid/hierarchical inheritance
# class Parent():
#     def property(self):
#         print("hello")
# class Son(Parent):
#     def name(self):
#         print("son")
# class Daughter(Parent):
#     def game(self):
#         print("daughter")
# A=Daughter()
# A.property()
# B=Son()
# B.property()

#multiple inheritance
# class Father():
#     def father_feature(self):
#         print("sports")
# class Mother():
#     def mother_feature(self):
#         print("cooking")
# class Son(Father, Mother):
#     def son_feature(self):
#         print("Jai mastan di")
# A=Son()
# A.father_feature()
# A.mother_feature()


#simple inheritance
# class Glass():
#     def func(self):
#         print("This man is very honest")

# class Plass(Glass):
#     def property(self):
#         print("Honesty is the best policy")
# gear=Plass()
# gear.func()

#multilevel inheritance
# class Father():
#     def income(self):
#         print("my income is 1000")
# class Son(Father):
#     def property(self,a,b):
#         print(a+b)
# class Child(Son):
#     def money():
#         print("i got 50 rs from Son")
# obj=Child()
# obj.property(5,6)
# obj.income()

# class Father():
#     def income(self,a,b):
#         print(a+b)
# class Son(Father):
#     def property(self,a,b):
#         print(a+b)
# class Child(Son):
#     def money():
#         print("i got 50 rs from Son")
# obj=Child()
# obj.property()
# obj.income(18,9)

#hybrid inheritance
# class Disc():
#     def function(self,a,b):
#         print(a+b)
# class Son(Disc):
#     def delta(self,a,b):
#         print(a+b)
# class Daughter(Disc):
#     def data(self,a,b):
#         print(a+b)
# obj=Son()
# obj.function(55,66)
# lean=Daughter()
# lean.function(78,89)

#multiple inheritance
# class Test():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def father(self):
#         print(self.a+self.b)
# class Code():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def mother(self):
#         print(self.a*self.b)
# class Child(Test, Code):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def son(self):
#         print("this is your son")
#         print(self.a-self.b)
# obj=Child(66,45)
# obj.father()
# obj.mother()
# obj.son()


#inheritance example
# class infinite():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def exam(self):
#         print(self.a+self.b)
# class cont(infinite):
#     def delta(self,a,b):
#         print(a*b)
# obj=cont(4,5)
# obj.exam()
# obj.delta(3,3)   






