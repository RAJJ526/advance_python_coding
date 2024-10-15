# duck typing
# class Dog:
#     def sounds(self):
#         print('dog')
# class Cat:
#     def sounds(self):
#         print('cat')
# class Sna:
#     def  walk(self):
#         print('walk')
# a  =  Dog()
# b  =  Cat()
# c  =  Sna()
# def call(*args):
#     for i in args:
#         if hasattr(i, 'sounds'):
#             i.sounds()
#         else:
#             print("404 error")
# call(a, b, c)


# class Fox:
#     def show(self):
#         print("fox")
# class Goat:
#     def dash(self):
#         print("goat")
# class Sheep:
#     def show(self):
#         print("sheep")

# def canon(*args):
#     for i in args:
#         if hasattr(i,"show"):
#             i.show()
#         else:
#             i.dash()
# a=Fox()
# b=Goat()
# c=Sheep()
# canon(a,b,c)


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
# kat(dog)
# kat(cat)

#another important example
# class Duck: #also called type of object
#     def quack(self):
#         return "quack quack"
    
#     def fly(self):
#         return " I am flying"
    
# class Penguin:
#     def quack(self):
#         return "hey! I am duck"
    
#     def fly(Self):
#         return "Hey! I am going to fly"
    
# def func(thing):
#     return thing.quack()

# def delta(thing):
#     return thing.fly()

    
# obj=Duck()
# job=Penguin()

# print(func(obj))
# print(func(job))




  


