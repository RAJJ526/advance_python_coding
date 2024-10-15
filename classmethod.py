class Drive:
    x="hello this is raj"
    y="welcome to class method"
    @classmethod
    def func(cls):
        print(cls.x, cls.y)
obj=Drive()
obj.func()

class Display:
    x="hello raj"
    y="hello kavita"
    @classmethod
    def func(cls):
        print(cls.x,cls.y)
    @staticmethod
    def kat(a,b):
        print(a+b)
obj=Display()
obj.func()
obj.kat(4,5)

#without class method
class Delta:
    v="the world is full of miseries"
    def word(self):
        print(self.v)
r=Delta()
r.word()

class Perform:
    c="the quieck jum over the lyz dog"
    @classmethod
    def func(cls):
        print(cls.c)
obj=Perform()
obj.func()

